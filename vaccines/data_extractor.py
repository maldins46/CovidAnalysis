#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts data from the vaccine repo per area.
@author: riccardomaldini
"""

import pandas as pd
import utils
from .population import population_dict as population
from . import areas


def extract_area_adm_data(area_code="ITA",
                          path='./VaccineOpenData/dati/somministrazioni-vaccini-summary-latest.csv'):
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
nation_data = extract_area_adm_data(areas.italia)
benchmark_regions_data = extract_benchmark_regions()
