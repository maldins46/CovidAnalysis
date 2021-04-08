#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts a dataframe that describes national-level data, making some analysis on it.
@author: riccardomaldini
"""

import pandas as pd
import dateutil.parser as date_parser
import utils
from data_extractors.ti_places import ti_places_dict
from data_extractors.population import population_dict
from data_extractors import istat_codes

# Constants
TI_PLACES_ITALY = ti_places_dict[istat_codes.italia]
POPULATION_ITALY = population_dict[istat_codes.italia]
RAW_DF = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')


def extract_italy_df():
    """
    Extracts a dataframe that describes nation-level data, making some analysis on it.
    :rtype: Dataframe
    """

    df = RAW_DF

    # convert data column in a proper date format
    df['data'] = df['data'].apply(lambda x: date_parser.parse(x))

    # Clean index and duplicates, sort by date
    df = df.sort_values('data')
    df = df[~df.data.duplicated(keep='last')]
    df = df.reset_index()
    df = df.drop('index', 1)

    # Filter data from September
    df = df[df['data'] > '2020-10-15']

    # TI occupation
    df['occupazione_ti'] = df['terapia_intensiva'] / TI_PLACES_ITALY

    # Positivity rate
    df['tamponi_giornalieri'] = df['tamponi'].diff()
    df.at[297, 'tamponi_giornalieri'] = 180000
    df['tamponi_positivi_giornalieri'] = df['totale_casi'].diff()
    df['tasso_positivita'] = df['tamponi_positivi_giornalieri'] / df['tamponi_giornalieri']

    # Recovered with symptoms per 100.000 inhabitants
    df['ric_per_100000_ab'] = df['ricoverati_con_sintomi'] / POPULATION_ITALY * 100000

    # New positives per 100.000 inhabitants
    df['nuovi_pos_per_100000_ab'] = df['nuovi_positivi'] / POPULATION_ITALY * 100000

    # Weekly incidence
    df['incidenza_settimanale'] = utils.distanced_diff(df['totale_casi'], 7)
    df['incid_sett_per_100000_ab'] = df['incidenza_settimanale'] / POPULATION_ITALY * 100000

    # Death increment
    df['incremento_morti'] = df['deceduti'].diff()
    df['incr_morti_per_100000_ab'] = df['incremento_morti'] / POPULATION_ITALY * 100000

    # R(t) SIRD
    df['rt'] = utils.compute_rt(df['totale_casi'], df['dimessi_guariti'], df['deceduti'])

    return df


# Pre-computed data. Use this to avoid re-generating the data structure each time
italy_df = extract_italy_df()
