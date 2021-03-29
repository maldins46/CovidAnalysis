#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts dataframes that describes regional-level data, making some analysis on it.
@author: riccardomaldini
"""

import pandas as pd
import os
import glob
import dateutil.parser as date_parser
from data_extractors import istat_codes
from data_extractors.ti_places import ti_places_dict
from data_extractors.population import population_dict
from data_extractors.istat_code_groups import benchmark_array
from data_extractors import istat_codes
from data_extractors.geojson import regions_geodf
import utils

# Constants
RAW_DF = pd.read_csv('./data/opendata-covid-italia/dati-regioni/dpc-covid19-ita-regioni.csv')


def extract_regions_df():
    """
    Extracts dataframes that describes regional-level data, making some analysis on it.
    :rtype: Dataframe
    """
    
    df = RAW_DF

    # convert data column in a proper date format
    df['data'] = df['data'].apply(lambda x: date_parser.parse(x))

    # Clean index and duplicates, sort by region and date
    df = df.sort_values(['codice_regione','data'])

    df['codice_regione'] = df['codice_regione'].apply(lambda x: f"{x:02d}")

    # Filter data from September
    df = df[df['data'] > '2020-09-15']

    # TI occupation
    df['occupazione_ti'] = df.apply(lambda x: x['terapia_intensiva'] / ti_places_dict[x['codice_regione']], axis=1)

    # Positivity rate
    df['tamponi_giornalieri'] = df['tamponi'].diff()
    df['tamponi_positivi_giornalieri'] = df['totale_casi'].diff()
    df['tasso_positivita'] = df['tamponi_positivi_giornalieri'] / df['tamponi_giornalieri']

    # Recovered with symptoms per 100.000 inhabitants
    df['ric_per_100000_ab'] = df.apply(lambda x: x['ricoverati_con_sintomi'] / population_dict[x['codice_regione']] * 100000, axis=1)

    # New positives per 100.000 inhabitants
    df['nuovi_pos_per_100000_ab'] = df.apply(lambda x: x['nuovi_positivi'] / population_dict[x['codice_regione']] * 100000, axis=1)

    # Weekly incidence
    df['incidenza_settimanale'] = utils.distanced_diff(df['totale_casi'], 7)
    df['incid_sett_per_100000_ab'] = df.apply(lambda x: x['incidenza_settimanale'] / population_dict[x['codice_regione']] * 100000, axis=1)

    # Death increment
    df['incremento_morti'] = df['deceduti'].diff()
    df['incr_morti_per_100000_ab'] = df.apply(lambda x: x['incremento_morti'] / population_dict[x['codice_regione']] * 100000, axis=1)

    # Filter data 15 days later (removes tail effect)
    df = df[df['data'] > '2020-10-15']

    return df


def extract_benchmark_dict(df):
    """
    Extract some specific regions defined as of interest in the analysis, as a dictionary.
    """

    dfs_dict = {}

    for region_code in benchmark_array:
        region_df = df[df['codice_regione'] == region_code]
        dfs_dict[region_code] = region_df

    return dfs_dict


def extract_regions_geodf(df):
    """
    Extracts relevant data for geographical plots, and marges them to the regional Geodataframe.
    """

    # select only tail (last version of data)
    summary_df = df.sort_values(['data'])
    summary_df = summary_df.tail(21)

    # Labels for maps
    summary_df['incid_sett_per_100000_round'] = summary_df['incid_sett_per_100000_ab'].apply(lambda x: round(x, 0))
    summary_df['incid_sett_per_100000_ab_label'] = summary_df['incid_sett_per_100000_round'].apply(lambda x: f"{x:.0f}")
    summary_df['occupazione_ti_100'] = summary_df['occupazione_ti'].apply(lambda x: x * 100)
    summary_df['occupazione_ti_label'] = summary_df['occupazione_ti_100'].apply(lambda x: f"{x:.2f} %")

    # Merge geo data to analysis
    merged_df = regions_geodf.merge(summary_df, on='codice_regione')

    # Add location for the labels
    merged_df['coords'] = merged_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    merged_df['coords'] = [coords[0] for coords in merged_df['coords']]

    return merged_df


# Pre-computed data. Use this to avoid re-generating the data structure each time
regions_df = extract_regions_df()
regions_geodf = extract_regions_geodf(regions_df)
benchmark_dict = extract_benchmark_dict(regions_df)
marche_df = benchmark_dict[istat_codes.marche]
