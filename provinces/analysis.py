#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid in marche.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
import numpy as np
from national.data_extractor import nation_data
from .data_extractor import provinces_of_marche_data


def compute_total_cases_per_provinces(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces.
    """

    for province_name, province in provinces_of_marche_data.items():
        dates, cases = compute_x_days_mov_average(province, 'incr_casi_per_100000_ab', 28)
        plt.plot(dates, cases, label=province_name)

    dates, cases = compute_x_days_mov_average(nation_data, 'nuovi_pos_per_100000_ab', 28)
    plt.plot(dates, cases, alpha=0.5, linestyle=':', label="Italia")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Nuovi positivi Marche (valori relativi)')
    plt.ylabel('Nuovi pos. ogni 100.000 ab. (1m. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/totale_casi_per_province_marche.png', dpi=300, transparent=True)

    if show:
        plt.show()

    plt.close()


def compute_total_cases_per_provinces_abs(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces, as absolute cases.
    """

    for province_name, province in provinces_of_marche_data.items():
        dates, cases = compute_x_days_mov_average(province, 'incremento_casi', 28)
        plt.plot(dates, cases, label=province_name)

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Nuovi positivi Marche (valori assoluti)')
    plt.ylabel('Nuovi pos. in val. ass. (1m. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/totale_casi_per_province_marche_abs.png', dpi=300, transparent=True)

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
