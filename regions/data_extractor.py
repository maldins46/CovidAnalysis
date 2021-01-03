#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts regional data from the database.
@author: riccardomaldini
"""

import pandas as pd
import os
import glob
import dateutil.parser as date_parser
from . import regions_names as reg
from .ti_places import ti_places_dict as ti_places
from .population import population_dict as population


def extract_regions_data(path='./GvtOpenData/dati-regioni'):
    """ Reads all csv files about regions data and concatenates them in a data frame."""

    all_files_paths = os.path.join(path, "*.csv")
    all_files = glob.glob(all_files_paths)
    return pd.concat((pd.read_csv(file) for file in all_files))


def extract_single_region_data(region):
    """
    Extracts all data about a single region, it sort them, and adds additional data about TI occupation, if available.
    Also, converts datesto datetime.
    """

    region_df = regions_data.loc[regions_data['denominazione_regione'] == region]

    # suppresses a false positive in the function
    pd.options.mode.chained_assignment = None

    # convert data column in a proper date format
    region_df['data'] = region_df['data'].map(lambda date_str: date_parser.parse(date_str))

    # re-activates warnings
    pd.options.mode.chained_assignment = 'warn'

    # Clean index and duplicates, sort by date
    region_df = region_df.sort_values('data')
    region_df = region_df[~region_df.data.duplicated(keep='last')]
    region_df = region_df.reset_index()
    region_df = region_df.drop('index', 1)

    # Filter data from September
    region_df = region_df[region_df['data'] > '2020-09-01']

    # Adds TI occupation data
    region_df['occupazione_ti'] = region_df['terapia_intensiva'] / ti_places[region]

    # Adds positivity rate
    region_df['tamponi_giornalieri'] = region_df['tamponi'].diff()
    region_df['tamponi_positivi_giornalieri'] = region_df['totale_casi'].diff()
    region_df['tasso_positivita'] = region_df['tamponi_positivi_giornalieri'] / region_df['tamponi_giornalieri']

    # Add data 'ricoverati con sintomi' per 100.000 inhabitants
    region_df['ric_per_100000_ab'] = region_df['ricoverati_con_sintomi'] / population[region] * 100000

    # Add data 'nuovi positivi' per 100.000 inhabitants
    region_df['nuovi_pos_per_100000_ab'] = region_df['nuovi_positivi'] / population[region] * 100000

    # Add data 'incremento morti', scale per 100.000 inhabitants
    region_df['incremento_morti'] = region_df['deceduti'].diff()
    region_df['incr_morti_per_100000_ab'] = region_df['incremento_morti'] / population[region] * 100000

    return region_df


def extract_benchmark_regions():
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """

    return {
        reg.lombardia: extract_single_region_data(reg.lombardia),
        reg.emilia_romagna: extract_single_region_data(reg.emilia_romagna),
        reg.marche: extract_single_region_data(reg.marche)
    }


# Create dataframe, extract some region data
regions_data = extract_regions_data()
benchmark_regions_data = extract_benchmark_regions()
