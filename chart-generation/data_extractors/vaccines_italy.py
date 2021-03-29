#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts dataframes that describes vaccines data, making some analysis on it.
@author: riccardomaldini
"""

import pandas as pd
import utils
from data_extractors import istat_codes
from data_extractors.population import population_dict


# Constants
POPULATION_ITALY = population_dict[istat_codes.italia]
RAW_DF = pd.read_csv('/users/riccardomaldini/Desktop/CovidAnalysis/data/opendata-vaccini-italia/dati/somministrazioni-vaccini-summary-latest.csv')

def extract_italy_df():
    """
    Extracts dataframes that describes national-level vaccines data, making some analysis on it.
    """

    df = RAW_DF

    # Group with sum for all fields
    df = df.groupby('data_somministrazione').sum()

    # Clean index and duplicates, sort by date
    df = df.sort_values('data_somministrazione')
    df = df.reset_index()

    # Filter data from September
    df = df[df['data_somministrazione'] >= '2021-01-01']

    # Doses per 100.000 inhabitants
    df['prima_dose_per_100000_ab'] = df['prima_dose'] / POPULATION_ITALY * 100000
    df['seconda_dose_per_100000_ab'] = df['seconda_dose'] / POPULATION_ITALY * 100000
    df['totale_per_100000_ab'] = df['totale'] / POPULATION_ITALY * 100000

    # Historical totals
    df['totale_storico'] = df['totale'].cumsum()
    df['totale_storico_su_pop'] = df['totale_storico'] / POPULATION_ITALY

    df['prima_dose_totale_storico'] = df['prima_dose'].cumsum()
    df['prima_dose_totale_storico_su_pop'] = df['prima_dose_totale_storico'] / POPULATION_ITALY

    df['seconda_dose_totale_storico'] = df['seconda_dose'].cumsum()
    df['seconda_dose_totale_storico_su_pop'] = df['seconda_dose_totale_storico'] / POPULATION_ITALY

    return df


# Pre-computed data. Use this to avoid re-generating the data structure each time
italy_df = extract_italy_df()
