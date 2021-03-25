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
from dictionaries import area_codes as areas
from dictionaries.area_names import area_names_dict as area_names
import utils
from dictionaries.ti_places import ti_places_dict as ti_places
from dictionaries.population import population_dict as population

def extract_map_data():
    """
    Extracts relevant data for geographical plots, and marges them to the regional Geodataframe.
    """

    # Extract last rilevation for each region
    summary_df = pd.DataFrame()
    for key, area in areas.regions_dict.items():
        last_rilevation = extract_single_region_data(area).tail(1)
        summary_df = pd.concat([summary_df, last_rilevation], sort=False, ignore_index=True).fillna(0)

    # Change Trento and Bolzano ISTAT code to match the GeoDataframe
    summary_df = summary_df.rename(columns={'codice_regione_ISTAT': 'codice_regione'})

    # Merge geo data to vaccine info
    geo_df = utils.get_clean_regions_geodf()
    merged_df = geo_df.merge(summary_df, on='codice_regione')

    return merged_df


def extract_single_region_data(region_code=areas.marche):
    """
    Extracts all data about a single region, it sort them, and adds additional data about TI occupation, if available.
    Also, converts datesto datetime.
    """
    area_name = area_names[region_code]
    region_df = regions_data.loc[regions_data['denominazione_regione'] == area_name]

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

    # Filter data from 4 months ago
    # import datetime
    # today = datetime.datetime.now()
    # d = datetime.timedelta(days=120)
    # four_months_ago = today - d

    # Filter data from September
    region_df = region_df[region_df['data'] > '2020-10-15']

    # Adds TI occupation data
    region_df['occupazione_ti'] = region_df['terapia_intensiva'] / ti_places[region_code]

    # Adds positivity rate
    region_df['tamponi_giornalieri'] = region_df['tamponi'].diff()
    region_df['tamponi_positivi_giornalieri'] = region_df['totale_casi'].diff()
    region_df['tasso_positivita'] = region_df['tamponi_positivi_giornalieri'] / region_df['tamponi_giornalieri']

    # Add data 'ricoverati con sintomi' per 100.000 inhabitants
    region_df['ric_per_100000_ab'] = utils.scale_per_x_inhabitants(region_df['ricoverati_con_sintomi'],
                                                                   population[region_code])

    # Add data 'nuovi positivi' per 100.000 inhabitants
    region_df['nuovi_pos_per_100000_ab'] = utils.scale_per_x_inhabitants(region_df['nuovi_positivi'], population[region_code])

    # Add data 'incremento morti', scale per 100.000 inhabitants
    region_df['incremento_morti'] = region_df['deceduti'].diff()
    region_df['incr_morti_per_100000_ab'] = utils.scale_per_x_inhabitants(region_df['incremento_morti'],
                                                                          population[region_code])

    # Add data 'incidenza settimanale, scale per 100.000 inhabitants
    region_df['incidenza_settimanale'] = utils.distanced_diff(region_df['totale_casi'], 7)
    region_df['incid_sett_per_100000_ab'] = utils.scale_per_x_inhabitants(region_df['incidenza_settimanale'],
                                                                          population[region_code])

    region_df['incid_sett_per_100000_ab'] = region_df.apply(lambda x: 500 if x['incid_sett_per_100000_ab'] > 500 else x['incid_sett_per_100000_ab'], axis=1)


    # compute rt
    region_df['rt'] = utils.compute_rt(region_df['totale_casi'], region_df['dimessi_guariti'], region_df['deceduti'])

    return region_df


def extract_benchmark_regions():
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """

    return {
        areas.toscana: extract_single_region_data(areas.toscana),
        areas.veneto: extract_single_region_data(areas.veneto),
        areas.marche: extract_single_region_data(areas.marche)
    }


# Create dataframe, extract some region data
regions_data = pd.read_csv('/users/riccardomaldini/Desktop/CovidAnalysis/GvtOpenData/dati-regioni/dpc-covid19-ita-regioni.csv')
benchmark_regions_data = extract_benchmark_regions()
