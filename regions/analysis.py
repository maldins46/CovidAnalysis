#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid.
@author: riccardomaldini
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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


# Create dataframe, extract some region data, plot all available info into files inside docs directory
df = extract_regions_data()


def extract_single_region_data(region):
    """
    Extracts all data about a single region, it sort them, and adds additional data about TI occupation, if available.
    Also, converts datesto datetime.
    """

    region_df = df.loc[df['denominazione_regione'] == region]

    # convert data column in a proper date format
    region_df['data'] = region_df['data'].map(lambda date_str: date_parser.parse(date_str)) 

    # sort values by date
    region_df = region_df.sort_values('data')

    # Adds TI occupation data
    region_df = region_df.assign(occupazione_ti=pd.Series(np.zeros(region_df.size)))
    region_df['occupazione_ti'] = region_df['terapia_intensiva'] / ti_places[region]

    # Remove some duplicated data
    region_df = region_df[~region_df.index.duplicated(keep=False)]

    # set dath increment column
    region_df['incremento_morti'] = region_df['deceduti'].diff()

    return region_df


def extract_regions_of_interest():
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """

    return {
        reg.lombardia: extract_single_region_data(reg.lombardia),
        reg.emilia_romagna: extract_single_region_data(reg.emilia_romagna),
        reg.molise: extract_single_region_data(reg.molise),
        reg.marche: extract_single_region_data(reg.marche)
    }


def compute_ti_occupation_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones, for some regions of interest.
    """

    regions = extract_regions_of_interest()

    for region_name, region in regions.items():
        plt.plot(region['data'], region['occupazione_ti'], label=region_name)

    plt.axhline(y=0.3, color='r', linestyle='--', label="Livello d'allerta")
    plt.axhline(y=1, color='y', linestyle='--', label="Saturazione")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Occupazione TI giornaliera per regioni')
    plt.xlabel('Date')
    plt.ylabel('Occupazione TI giornaliera')
    plt.legend()

    if save_image:
        plt.savefig('./docs/ti_per_regioni.png', dpi=300)

    if show:
        plt.show()

    plt.close()


def compute_rec_with_symptoms(save_image=False, show=False):
    """
    Computes and plots recovered with symptoms.
    """

    regions = extract_regions_of_interest()

    for region_name, region in regions.items():
        plt.plot(region['data'], region['ricoverati_con_sintomi'], label=region_name)

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Ricoverati con sintomi giornalieri per regioni')
    plt.xlabel('Date')
    plt.ylabel('Ricoverati con sintomi')
    plt.legend()

    if save_image:
        plt.savefig('./docs/ricoverati_con_sintomi_per_regioni.png', dpi=300)

    if show:
        plt.show()

    plt.close()


def compute_daily_cases(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones, for some regions of interest.
    """

    regions = extract_regions_of_interest()

    for region_name, region in regions.items():
        dates, pos = compute_x_days_mov_average(region, 'nuovi_positivi', 7)
        plt.plot(dates, pos, label=region_name)

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Nuovi positivi giornalieri per regione (7 gg. m.a.)')
    plt.xlabel('Date')
    plt.ylabel('Nuovi positivi')
    plt.legend()

    if save_image:
        plt.savefig('./docs/positivi_per_regioni.png', dpi=300)

    if show:
        plt.show()

    plt.close()


def compute_death(save_image=False, show=False):
    """
    Computes and plots daily deaths.
    """

    regions = extract_regions_of_interest()

    for region_name, region in regions.items():
        dates, deaths = compute_x_days_mov_average(region, 'incremento_morti', 7)
        plt.plot(dates, deaths, label=region_name)

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Deceduti giornalieri per regioni (7 gg. m.a.)')
    plt.xlabel('Date')
    plt.ylabel('Deceduti')
    plt.legend()

    if save_image:
        plt.savefig('./docs/deceduti_per_regioni.png', dpi=300)

    if show:
        plt.show()

    plt.close()


def compute_x_days_mov_average(df, column, window=7):
    """
    Computes an x-days-moving-average on the given column, of the given
    dataframe, and returns the computed column and the correspondant dates,
    for plotting.
    """

    column_ma = np.convolve(df[column], np.ones(window)/window, mode='valid')
    dates = df.iloc[window-1:].data

    return dates, column_ma
