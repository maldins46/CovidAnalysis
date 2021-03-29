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
from data_extractors.istat_code_groups import benchmark_array, regions_array
from data_extractors.geojson import regions_geodf
import geopandas as gpd

# Constants and pre-cleaning
RAW_DF = pd.read_csv('./data/opendata-vaccini-italia/dati/somministrazioni-vaccini-summary-latest.csv')
RAW_DF['codice_regione_ISTAT'] = RAW_DF.apply(lambda x: 21 if x['area'] == 'PAT' else x['codice_regione_ISTAT'], axis=1)
RAW_DF['codice_regione_ISTAT'] = RAW_DF.apply(lambda x: 22 if x['area'] == 'PAB' else x['codice_regione_ISTAT'], axis=1)
RAW_DF['codice_regione_ISTAT'] = RAW_DF['codice_regione_ISTAT'].apply(lambda x: f"{x:02d}")


def extract_region_df(region_code="11"):
    """
    Extracts dataframes that describes regional-level vaccines data for a single region, making some analysis on it.
    :rtype: Dataframe
    """

    df = RAW_DF

    df = df.loc[df['codice_regione_ISTAT'] == region_code]
    
    df = df.sort_values('data_somministrazione')
    df = df.reset_index()

    # Filter data from September
    df = df[df['data_somministrazione'] >= '2021-01-01']

    # Doses per 100.000 inhabitants
    df['prima_dose_per_100000_ab'] = df.apply(lambda x: x['prima_dose'] / population_dict[x['codice_regione_ISTAT']] * 100000, axis=1)
    df['seconda_dose_per_100000_ab'] = df.apply(lambda x: x['seconda_dose'] / population_dict[x['codice_regione_ISTAT']] * 100000, axis=1)
    df['totale_per_100000_ab'] = df.apply(lambda x: x['totale'] / population_dict[x['codice_regione_ISTAT']] * 100000, axis=1)

    # Historical totals
    df['totale_storico'] = df['totale'].cumsum()
    df['totale_storico_su_pop'] = df.apply(lambda x: x['totale_storico'] / population_dict[x['codice_regione_ISTAT']], axis=1)

    df['prima_dose_totale_storico'] = df['prima_dose'].cumsum()
    df['prima_dose_totale_storico_su_pop'] = df.apply(lambda x: x['prima_dose_totale_storico'] / population_dict[x['codice_regione_ISTAT']], axis=1)

    df['seconda_dose_totale_storico'] = df['seconda_dose'].cumsum()
    df['seconda_dose_totale_storico_su_pop'] = df.apply(lambda x: x['seconda_dose_totale_storico'] / population_dict[x['codice_regione_ISTAT']], axis=1)

    return df


def extract_regions_geodf():
    """
    Extracts relevant data for geographical plots, and marges them to the regional Geodataframe.
    """
    
    # Extract last rilevation for each region
    df = pd.DataFrame()
    for region_code in regions_array:
        last_rilevation = extract_region_df(region_code).tail(1)
        df = pd.concat([df, last_rilevation], sort=False, ignore_index=True).fillna(0)

    # Change Trento and Bolzano ISTAT code to match the GeoDataframe
    df = df.rename(columns={'codice_regione_ISTAT': 'codice_regione'})

    df['seconda_dose_totale_storico_su_pop_100'] = df.apply(lambda x: x['seconda_dose_totale_storico_su_pop'] * 100, axis=1)
    df['seconda_dose_totale_storico_su_pop_label'] = df.apply(lambda x: f"{x['seconda_dose_totale_storico_su_pop_100']:.2f} %", axis=1)
    
    # Merge geo data to analysis
    merged_df = regions_geodf.merge(df, on='codice_regione')

    # Add location for the labels
    merged_df['coords'] = merged_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    merged_df['coords'] = [coords[0] for coords in merged_df['coords']]

    return merged_df



def extract_benchmark_dict():
    """
    Extract some specific regions defined as of interest in the analysis, as a dictionary.
    """

    dfs_dict = {}

    for region_code in benchmark_array:
        df = extract_region_df(region_code)
        dfs_dict[region_code] = df

    return dfs_dict


# Pre-computed data. Use this to avoid re-generating the data structure each time
regions_geodf = extract_regions_geodf()
benchmark_dict = extract_benchmark_dict()
marche_df = benchmark_dict[istat_codes.marche]