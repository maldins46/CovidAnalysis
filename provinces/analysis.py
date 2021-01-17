#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid in marche.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
from national.data_extractor import nation_data
from .data_extractor import provinces_of_marche_data
from regions.data_extractor import extract_single_region_data
from regions import regions_names
import utils

marche_data = extract_single_region_data(regions_names.marche)


def compute_total_cases_per_provinces(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces.
    """

    for province_name, province_data in provinces_of_marche_data.items():
        cases = utils.compute_x_days_mov_average(province_data['incr_casi_per_100000_ab'], 14)
        plt.plot(province_data['data'], cases, label=province_name)

    cases = utils.compute_x_days_mov_average(nation_data['nuovi_pos_per_100000_ab'], 14)
    plt.plot(nation_data['data'], cases, alpha=0.5, linestyle=':', label="Italia")

    cases = utils.compute_x_days_mov_average(marche_data['nuovi_pos_per_100000_ab'], 14)
    plt.plot(marche_data['data'], cases, alpha=0.5, linestyle=':', label="Marche")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Nuovi pos. ogni 100.000 ab. (14 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/totale_casi_per_province_marche.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_total_cases_per_provinces_abs(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces, as absolute cases.
    """

    for province_name, province_data in provinces_of_marche_data.items():
        cases = utils.compute_x_days_mov_average(province_data['incremento_casi'], 14)
        plt.plot(province_data['data'], cases, label=province_name)

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Nuovi pos. in val. ass. (14 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/totale_casi_per_province_marche_abs.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
