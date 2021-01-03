#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid.
@author: riccardomaldini
"""

import numpy as np
import matplotlib.pyplot as plt
from .data_extractor import nation_data


def compute_national_parameters(save_image=False, show=False):
    """
    Different data about Italy.
    """

    dates, deaths = compute_x_days_mov_average(nation_data, 'incremento_morti', 7)
    plt.plot(dates, deaths, label='Incremento morti (7 gg. m.a.)')

    plt.plot(nation_data['data'], nation_data['terapia_intensiva'], label='Pazienti TI')

    dates, pos = compute_x_days_mov_average(nation_data, 'nuovi_positivi', 7)
    plt.plot(dates, pos, label="Nuovi positivi (7 gg. m.a.)")

    plt.plot(nation_data['data'], nation_data['ricoverati_con_sintomi'], label="Ricoverati con sintomi")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.ylabel('Variaz. parametri')
    plt.legend()

    if save_image:
        plt.savefig('./docs/parametri_italia.png', dpi=300, transparent=True, bbox_inches='tight')

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
