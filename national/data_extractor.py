#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts national data from the database.
@author: riccardomaldini
"""

import pandas as pd
import os
import glob
import dateutil.parser as date_parser
import utils
from dictionaries.area_codes import italia
from dictionaries.population import population_dict
from dictionaries.ti_places import ti_places_dict

ti_places = ti_places_dict[italia]
population = population_dict[italia]


def extract_nation_data(path='./GvtOpenData/dati-andamento-nazionale'):
    """
    Reads all csv files about regions data and concatenates them in a data frame.
    """

    all_files_paths = os.path.join(path, "*.csv")
    all_files = glob.glob(all_files_paths)
    national_df = pd.concat((pd.read_csv(file) for file in all_files))

    # suppresses a false positive in the function
    pd.options.mode.chained_assignment = None

    # convert data column in a proper date format
    national_df['data'] = national_df['data'].map(lambda date_str: date_parser.parse(date_str))

    # re-activates warnings
    pd.options.mode.chained_assignment = 'warn'

    # Clean index and duplicates, sort by date
    national_df = national_df.sort_values('data')
    national_df = national_df[~national_df.data.duplicated(keep='last')]
    national_df = national_df.reset_index()
    national_df = national_df.drop('index', 1)

    # Filter data from September
    national_df = national_df[national_df['data'] > '2020-09-01']

    # Adds TI occupation data
    national_df['occupazione_ti'] = national_df['terapia_intensiva'] / ti_places

    # Adds positivity rate
    national_df['tamponi_giornalieri'] = national_df['tamponi'].diff()

    # custom cleaning for some dirty data
    national_df.at[297, 'tamponi_giornalieri'] = 180000

    national_df['tamponi_positivi_giornalieri'] = national_df['totale_casi'].diff()
    national_df['tasso_positivita'] = national_df['tamponi_positivi_giornalieri'] / national_df['tamponi_giornalieri']

    # Add data 'ricoverati con sintomi' per 100.000 inhabitants
    national_df['ric_per_100000_ab'] = utils.scale_per_x_inhabitants(national_df['ricoverati_con_sintomi'], population)

    # Add data 'nuovi positivi' per 100.000 inhabitants
    national_df['nuovi_pos_per_100000_ab'] = utils.scale_per_x_inhabitants(national_df['nuovi_positivi'], population)

    # Add data 'incidenza settimanale, scale per 100.000 inhabitants
    national_df['incidenza_settimanale'] = utils.distanced_diff(national_df['totale_casi'], 7)
    national_df['incid_sett_per_100000_ab'] = utils.scale_per_x_inhabitants(national_df['incidenza_settimanale'], population)

    # Add data 'incremento morti', scale per 100.000 inhabitants
    national_df['incremento_morti'] = national_df['deceduti'].diff()
    national_df['incr_morti_per_100000_ab'] = utils.scale_per_x_inhabitants(national_df['incremento_morti'], population)

    # compute rt
    national_df['rt'] = utils.compute_rt(national_df['totale_casi'], national_df['dimessi_guariti'], national_df['deceduti'])

    return national_df


# Create dataframe with national data
nation_data = extract_nation_data()
