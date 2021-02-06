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


def extract_provinces_data(path='./GvtOpenData/dati-province'):
    """
    Reads all csv files about provinces data and concatenates them in a data frame.
    """

    all_files_paths = os.path.join(path, "*.csv")
    all_files = glob.glob(all_files_paths)
    return pd.concat((pd.read_csv(file) for file in all_files))


def extract_single_province_data(province_code="ANC"):
    """
    Extracts all data about a single province, it sort them, and adds. Also, converts dates to datetime.
    """

    area_name = area_names[province_code]
    province_df = provinces_data.loc[provinces_data['denominazione_provincia'] == area_name]

    # suppresses a false positive in the function
    pd.options.mode.chained_assignment = None

    # convert data column in a proper date format
    province_df['data'] = province_df['data'].map(lambda date_str: date_parser.parse(date_str))

    # re-activates warnings
    pd.options.mode.chained_assignment = 'warn'

    # Clean index and duplicates, sort by date
    province_df = province_df.sort_values('data')
    province_df = province_df[~province_df.data.duplicated(keep='last')]
    province_df = province_df.reset_index()
    province_df = province_df.drop('index', 1)

    # Filter data from September
    province_df = province_df[province_df['data'] > '2020-10-15']

    # Add data 'incremento casi', scale per 100000 inhabitants
    province_df['incremento_casi'] = province_df['totale_casi'].diff()

    # custom cleaning for some dirty data
    province_df['incremento_casi'] = province_df['incremento_casi'].apply(lambda x: x if x > 0 else float('NaN'))
    province_df['incremento_casi'] = province_df['incremento_casi'].apply(lambda x: x if x < 400 else float('NaN'))
    province_df['incremento_casi'] = province_df['incremento_casi'].fillna(method='ffill', limit=3)

    province_df['incr_casi_per_100000_ab'] = utils.scale_per_x_inhabitants(province_df['incremento_casi'],
                                                                           population[province_code])
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
provinces_data = extract_provinces_data()
provinces_of_marche_data = extract_provinces_of_marche()
