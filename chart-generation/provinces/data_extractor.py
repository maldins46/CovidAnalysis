#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts provincial data for Marche region from the database.
@author: riccardomaldini
"""

import pandas as pd
import os
import glob
import dateutil.parser as date_parser
import utils
from dictionaries import area_codes as areas
from dictionaries.area_names import area_names_dict as area_names
from dictionaries.population import population_dict as population

def extract_full_data():
    provinces_df = pd.read_csv('/users/riccardomaldini/Desktop/CovidAnalysis/GvtOpenData/dati-province/dpc-covid19-ita-province.csv')
    pop = utils.get_population_dict()

    # suppresses a false positive in the function
    pd.options.mode.chained_assignment = None

    # convert data column in a proper date format
    provinces_df['data'] = provinces_df['data'].map(lambda date_str: date_parser.parse(date_str))

    # re-activates warnings
    pd.options.mode.chained_assignment = 'warn'

    # Clean index and duplicates, sort by date
    provinces_df = provinces_df.sort_values(['codice_provincia','data'])

    # Filter data from September
    provinces_df = provinces_df[provinces_df['data'] > '2020-10-01']

    # Add data 'incidenza settimanale, scale per 100.000 inhabitants
    provinces_df = provinces_df[provinces_df['denominazione_provincia'] != 'Fuori Regione / Provincia Autonoma']
    provinces_df = provinces_df[provinces_df['denominazione_provincia'] != 'In fase di definizione/aggiornamento']
    

    # Add data 'incremento casi', scale per 100000 inhabitants
    provinces_df['incremento_casi'] = provinces_df['totale_casi'].diff()

    # custom cleaning for some dirty data
    provinces_df['incremento_casi'] = provinces_df['incremento_casi'].apply(lambda x: x if x > 0 else float('NaN'))
    provinces_df['incremento_casi'] = provinces_df['incremento_casi'].apply(lambda x: x if x < 400 else float('NaN'))
    provinces_df['incremento_casi'] = provinces_df['incremento_casi'].fillna(method='ffill', limit=3)
    
    provinces_df['incr_casi_per_100000_ab'] = provinces_df.apply(lambda x: x['incremento_casi'] / int(pop[x['denominazione_provincia']]) * 100000, axis=1)

    provinces_df['incidenza_settimanale'] = utils.distanced_diff(provinces_df['totale_casi'], 7)
    provinces_df['incid_sett_per_100000_ab'] = provinces_df.apply(lambda x: x['incidenza_settimanale'] / int(pop[x['denominazione_provincia']]) * 100000, axis=1)

    # Filter data 15 days later (removes tail effect)
    provinces_df = provinces_df[provinces_df['data'] > '2020-10-01']

    return provinces_df


def extract_map_data():
    """
    Extracts relevant data for geographical plots, and marges them to the regional Geodataframe.
    """

    # select only tail
    summary_df = provinces_data.sort_values(['data'])
    summary_df = summary_df.tail(107)

    # Other data for maps
    summary_df['incid_sett_per_100000'] = summary_df.apply(lambda x: round(x['incid_sett_per_100000_ab'], 0), axis=1)
    summary_df['incid_sett_per_100000_ab_label'] = summary_df.apply(lambda x: f"{x['incid_sett_per_100000_ab']:.0f}", axis=1)


    summary_df = summary_df.rename(columns={'codice_provincia': 'prov_istat_code_num'})

    # Merge geo data to vaccine info
    geo_df = utils.get_provinces_geodf()
    merged_df = geo_df.merge(summary_df, on='prov_istat_code_num')

    return merged_df


def extract_single_province_data(province_code="AN"):
    """
    Extracts all data about a single province, it sort them, and adds. Also, converts dates to datetime.
    """
    area_name = area_names[province_code]
    province_df = provinces_data.loc[provinces_data['denominazione_provincia'] == area_name]
    return province_df


def extract_provinces_of_marche():
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """
    return {
        areas.pesaro_urbino: extract_single_province_data(areas.pesaro_urbino),
        areas.macerata: extract_single_province_data(areas.macerata),
        areas.fermo: extract_single_province_data(areas.fermo),
        areas.ascoli_piceno: extract_single_province_data(areas.ascoli_piceno),
        areas.ancona: extract_single_province_data(areas.ancona)
    }


# Create dataframe, extract data for provinces of Marche
provinces_data = extract_full_data()
provinces_of_marche_data = extract_provinces_of_marche()
