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

ti_places = 6458
population = 60244639


def extract_national_data(path='./GvtOpenData/dati-andamento-nazionale'):
    """
    Reads all csv files about regions data and concatenates them in a data frame.
    """

    all_files_paths = os.path.join(path, "*.csv")
    all_files = glob.glob(all_files_paths)
    national_df = pd.concat((pd.read_csv(file) for file in all_files))

    # convert data column in a proper date format
    national_df['data'] = national_df['data'].map(lambda date_str: date_parser.parse(date_str))

    # sort values by date
    national_df = national_df.sort_values('data')

    # re-activates warnings
    pd.options.mode.chained_assignment = 'warn'

    # Remove some duplicated data
    national_df = national_df[~national_df.index.duplicated(keep=False)]

    # Adds TI occupation data, scale per 100.000 inhabitants
    national_df['occupazione_ti'] = national_df['terapia_intensiva'] / ti_places
    national_df['occ_ti_per_100000_ab'] = national_df['terapia_intensiva'] / population * 100000

    # Add data 'ricoverati con sintomi' per 100.000 inhabitants
    national_df['ric_per_100000_ab'] = national_df['ricoverati_con_sintomi'] / population * 100000

    # Add data 'nuovi positivi' per 100.000 inhabitants
    national_df['nuovi_pos_per_100000_ab'] = national_df['nuovi_positivi'] / population * 100000

    # Add data 'incremento morti', scale per 100.000 inhabitants
    national_df['incremento_morti'] = national_df['deceduti'].diff()
    national_df['incr_morti_per_100000_ab'] = national_df['incremento_morti'] / population * 100000

    return national_df


# Create dataframe, extract data, plot all available info into files inside docs directory
df = extract_national_data()


def compute_national_data(save_image=False, show=False):
    """
    Different data about Italy.
    """

    dates, deaths = compute_x_days_mov_average(df, 'incremento_morti', 7)
    plt.plot(dates, deaths, label='Incremento morti (7 gg. m.a.)')

    plt.plot(df['data'], df['terapia_intensiva'], label='Pazienti TI')

    dates, pos = compute_x_days_mov_average(df, 'nuovi_positivi', 7)
    plt.plot(dates, pos, label="Nuovi positivi (7 gg. m.a.)")

    plt.plot(df['data'], df['ricoverati_con_sintomi'], label="Ricoverati con sintomi")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Parametri COVID-19 Italia')
    plt.xlabel('Date')
    plt.ylabel('Variaz. parametri')
    plt.legend()

    if save_image:
        plt.savefig('./docs/parametri_italia.png', dpi=300, transparent=True)

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
