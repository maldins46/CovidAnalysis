#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analysis on the national vaccine data.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
# import matplotlib.ticker as mtick
from matplotlib.dates import MonthLocator, DateFormatter
# from .. import areas
# from ..data_extractor import benchmark_regions_data, extract_area_adm_data
from ..data_extractor import nation_data
# import utils


def compute_national_adm(save_image=False, show=False):
    """
    Administration data about Italy.
    """
    plt.bar(nation_data['data_somministrazione'], nation_data['prima_dose'], label='Prime dosi')
    plt.bar(nation_data['data_somministrazione'], nation_data['seconda_dose'], bottom=nation_data['prima_dose'],
            label='Seconde dosi')

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')

    plt.ylabel('Dosi giornaliere')
    plt.legend()

    if save_image:
        plt.savefig('./docs/dosi_somministrate.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
