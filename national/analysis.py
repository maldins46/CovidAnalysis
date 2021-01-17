#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
from .data_extractor import nation_data
import utils


def compute_national_parameters(save_image=False, show=False):
    """
    Different data about Italy.
    """

    deaths = utils.compute_x_days_mov_average(nation_data['incremento_morti'], 7)
    plt.plot(nation_data['data'], deaths, label='Nuovi decessi (7 gg. m.a.)')

    plt.plot(nation_data['data'], nation_data['terapia_intensiva'], label='Pazienti TI')

    pos = utils.compute_x_days_mov_average(nation_data['nuovi_positivi'], 7)
    plt.plot(nation_data['data'], pos, label="Nuovi positivi (7 gg. m.a.)")

    plt.plot(nation_data['data'], nation_data['ricoverati_con_sintomi'], label="Ricoverati con sintomi")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')

    plt.ylabel('Variaz. parametri')
    plt.legend()

    if save_image:
        plt.savefig('./docs/parametri_italia.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
