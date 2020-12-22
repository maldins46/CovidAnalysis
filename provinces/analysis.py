#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid in marche.
@author: riccardomaldini
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import dateutil.parser as date_parser
from . import provinces_names as prov
import numpy as np


def extract_provinces_data(path='./GvtOpenData/dati-province'):
    """
    Reads all csv files about provinces data and concatenates them in a data frame.
    """

    all_files_paths = os.path.join(path, "*.csv")
    all_files = glob.glob(all_files_paths)
    return pd.concat((pd.read_csv(file) for file in all_files))


# Create dataframe, extract some region data, plot all available info into files inside docs directory
df_provinces = extract_provinces_data()


def extract_single_province_data(province):
    """
    Extracts all data about a single province, it sort them, and adds. Also, converts dates to datetime.
    """

    # suppresses a false positive in the function
    pd.options.mode.chained_assignment = None

    province_df = df_provinces[df_provinces['denominazione_provincia'] == province]

    for index, row in province_df.iterrows():
        province_df.at[index, 'data'] = date_parser.parse(row['data'])

    province_df = province_df.sort_values('data')

    # re-activates warnings
    pd.options.mode.chained_assignment = 'warn'

    # Remove some duplicated data
    province_df = province_df[~province_df.index.duplicated(keep=False)]

    # makes diff on total cases
    province_df['casi'] = province_df['totale_casi'].diff()
    province_df = province_df[province_df['casi'] > 0]
    province_df = province_df[province_df['casi'] < 400]

    return province_df


def extract_provinces_of_marche():
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """
    return {
        prov.ancona: extract_single_province_data(prov.ancona),
        prov.pesaro_urbino: extract_single_province_data(prov.pesaro_urbino),
        prov.macerata: extract_single_province_data(prov.macerata),
        prov.fermo: extract_single_province_data(prov.fermo),
        prov.ascoli_piceno: extract_single_province_data(prov.ascoli_piceno)
    }


def compute_total_cases_per_provinces(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces.
    """

    provinces = extract_provinces_of_marche()

    for province_name, province in provinces.items():
        dates, cases = compute_x_days_mov_average(province, 'casi', 7)
        plt.plot(dates, cases, label=province_name)

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Casi per province delle Marche (7 gg. m.a.)')
    plt.xlabel('Date')
    plt.ylabel('Totale casi')
    plt.legend()

    if save_image:
        plt.savefig('./docs/totale_casi_per_province_marche.png', dpi=300)

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
