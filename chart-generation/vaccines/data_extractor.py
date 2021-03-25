#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts data from the vaccine repo per area.
@author: riccardomaldini
"""

import pandas as pd
import utils
from dictionaries.population import population_dict as population
from dictionaries import area_codes as areas
import geopandas as gpd


def extract_map_data():
    """
    Extracts relevant data for geographical plots, and marges them to the regional Geodataframe.
    """

    # Extract last rilevation for each region
    summary_df = pd.DataFrame()
    for key, area in areas.regions_dict.items():
        last_rilevation = extract_area_adm_data(area).tail(1)
        summary_df = pd.concat([summary_df, last_rilevation], sort=False, ignore_index=True).fillna(0)

    # Change Trento and Bolzano ISTAT code to match the GeoDataframe
    summary_df = summary_df.rename(columns={'codice_regione_ISTAT': 'codice_regione'})
    summary_df['codice_regione'] = summary_df.apply(lambda x: 21 if x['area'] == 'PAT' else x['codice_regione'], axis=1)
    summary_df['codice_regione'] = summary_df.apply(lambda x: 22 if x['area'] == 'PAB' else x['codice_regione'], axis=1)

    # Merge geo data to vaccine info
    geo_df = utils.get_clean_regions_geodf()
    merged_df = geo_df.merge(summary_df, on='codice_regione')

    return merged_df


def extract_national_data(path='/users/riccardomaldini/Desktop/CovidAnalysis/VaccineOpenData/dati/somministrazioni-vaccini-summary-latest.csv'):
    """
    Reads the data summary from the database and saves it in a data frame.
    """
    area_code = areas.italia
    adm_df = pd.read_csv(path)

    area_df = adm_df.groupby('data_somministrazione').sum()

    # Clean index and duplicates, sort by date
    area_df = area_df.sort_values('data_somministrazione')
    area_df = area_df.reset_index()

    # Filter data from September
    area_df = area_df[area_df['data_somministrazione'] >= '2021-01-01']

    # Doses per 100.000 ab
    area_df['prima_dose_per_100000_ab'] = utils.scale_per_x_inhabitants(area_df['prima_dose'], population[area_code])
    area_df['seconda_dose_per_100000_ab'] = utils.scale_per_x_inhabitants(area_df['seconda_dose'], population[area_code])
    area_df['totale_per_100000_ab'] = utils.scale_per_x_inhabitants(area_df['totale'], population[area_code])

    # Perc. doses per population
    area_df['perc_prima_dose'] = area_df['prima_dose'] / population[area_code]
    area_df['perc_seconda_dose'] = area_df['seconda_dose'] / population[area_code]
    area_df['perc_totale'] = area_df['totale'] / population[area_code]

    # Accumulation
    area_df['acc_totale'] = area_df['totale'].cumsum()
    area_df['acc_perc_totale'] = area_df['acc_totale'] / population[area_code]

    area_df['acc_prima_dose'] = area_df['prima_dose'].cumsum()
    area_df['acc_perc_prima_dose'] = area_df['acc_prima_dose'] / population[area_code]

    area_df['acc_seconda_dose'] = area_df['seconda_dose'].cumsum()
    area_df['acc_perc_seconda_dose'] = area_df['acc_seconda_dose'] / population[area_code]

    return area_df


def extract_area_adm_data(area_code="MAR",
                          path='/users/riccardomaldini/Desktop/CovidAnalysis/VaccineOpenData/dati/somministrazioni-vaccini-summary-latest.csv'):
    """
    Reads the data summary from the database and saves it in a data frame.
    """
    adm_df = pd.read_csv(path)
    area_df = adm_df.loc[adm_df['area'] == area_code]

    # Clean index and duplicates, sort by date
    area_df = area_df.sort_values('data_somministrazione')
    area_df = area_df.reset_index()
    area_df = area_df.drop('index', 1)

    # Filter data from September
    area_df = area_df[area_df['data_somministrazione'] >= '2021-01-01']

    # Doses per 100.000 ab
    area_df['prima_dose_per_100000_ab'] = utils.scale_per_x_inhabitants(area_df['prima_dose'], population[area_code])
    area_df['seconda_dose_per_100000_ab'] = utils.scale_per_x_inhabitants(area_df['seconda_dose'], population[area_code])
    area_df['totale_per_100000_ab'] = utils.scale_per_x_inhabitants(area_df['totale'], population[area_code])

    # Perc. doses per population
    area_df['perc_prima_dose'] = area_df['prima_dose'] / population[area_code]
    area_df['perc_seconda_dose'] = area_df['seconda_dose'] / population[area_code]
    area_df['perc_totale'] = area_df['totale'] / population[area_code]

    # Accumulation
    area_df['acc_totale'] = area_df['totale'].cumsum()
    area_df['acc_perc_totale'] = area_df['acc_totale'] / population[area_code]

    area_df['acc_prima_dose'] = area_df['prima_dose'].cumsum()
    area_df['acc_perc_prima_dose'] = area_df['acc_prima_dose'] / population[area_code]

    area_df['acc_seconda_dose'] = area_df['seconda_dose'].cumsum()
    area_df['acc_perc_seconda_dose'] = area_df['acc_seconda_dose'] / population[area_code]

    return area_df


def extract_benchmark_regions():
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """

    return {
        areas.toscana: extract_area_adm_data(areas.toscana),
        areas.veneto: extract_area_adm_data(areas.veneto),
        areas.marche: extract_area_adm_data(areas.marche)
    }


# Create dataframe, extract some data
nation_data = extract_national_data()
benchmark_regions_data = extract_benchmark_regions()
