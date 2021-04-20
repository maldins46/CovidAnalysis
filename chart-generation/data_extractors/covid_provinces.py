#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts dataframes that describes provincial-level data, making some analysis on it.
@author: riccardomaldini
"""

import pandas as pd
import dateutil.parser as date_parser
import utils
from data_extractors import istat_codes
from data_extractors.population import population_dict
from data_extractors.istat_code_groups import marche_array
from data_extractors.geojson import provinces_geodf as raw_provinces_geodf

# Constants
RAW_DF = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv')


def extract_provinces_df():
    """
    Extracts dataframes that describes provincial-level data, making some analysis on it.
    :rtype: Dataframe
    """

    df = RAW_DF

    # convert data column in a proper date format
    df['data'] = df['data'].apply(lambda x: date_parser.parse(x))

    # Clean index and duplicates, sort by date
    df = df.sort_values(['codice_provincia', 'data'])

    # Format code as text
    df['codice_provincia'] = df['codice_provincia'].apply(lambda x: f"{x:03d}")

    # Filter data from September
    df = df[df['data'] > '2020-10-01']

    # Remove dirty province data
    df = df[df['denominazione_provincia'] != 'Fuori Regione / Provincia Autonoma']
    df = df[df['denominazione_provincia'] != 'In fase di definizione/aggiornamento']

    # New positives
    df['nuovi_positivi'] = df['totale_casi'].diff()
    df['nuovi_positivi'] = df['nuovi_positivi'].apply(lambda x: x if x > 0 else float('NaN'))
    df['nuovi_positivi'] = df['nuovi_positivi'].apply(lambda x: x if x < 400 else float('NaN'))
    df['nuovi_positivi'] = df['nuovi_positivi'].fillna(method='ffill', limit=3)
    df['nuovi_pos_per_100000_ab'] = df.apply(lambda x: x['nuovi_positivi'] / population_dict[x['codice_provincia']] * 100000,
                                             axis=1)

    # Weekly incidence
    df['incidenza_settimanale'] = utils.distanced_diff(df['totale_casi'], 7)
    df['incid_sett_per_100000_ab'] = df.apply(lambda x: x['incidenza_settimanale'] / population_dict[x['codice_provincia']]
                                              * 100000, axis=1)

    df['incremento_incidenza'] = df['incidenza_settimanale'].rolling(7).apply(lambda x: (x.values[-1]-x.values[-7])/x.values[-7])

    # Filter data 15 days later (removes tail effect)
    df = df[df['data'] > '2020-10-15']

    return df


def extract_provinces_geodf(df):
    """
    Extracts relevant data for geographical plots, and marges them to the regional Geodataframe.
    """

    # select only tail (last version of data)
    summary_df = df.sort_values(['data'])
    summary_df = summary_df.tail(107)

    # Merge geo data to analysis
    merged_df = raw_provinces_geodf.merge(summary_df, on='codice_provincia')

    # Add location for the labels
    merged_df['coords'] = merged_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    merged_df['coords'] = [coords[0] for coords in merged_df['coords']]

    return merged_df


def extract_marche_dict(df):
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """

    dfs_dict = {}

    for province_code in marche_array:
        province_df = df[df['codice_provincia'] == province_code]
        dfs_dict[province_code] = province_df

    return dfs_dict


# Create dataframe, extract data for provinces of Marche
provinces_df = extract_provinces_df()
provinces_geodf = extract_provinces_geodf(provinces_df)
marche_geodf = provinces_geodf[provinces_geodf['reg_istat_code'] == istat_codes.marche]
marche_dict = extract_marche_dict(provinces_df)
