#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid in marche.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator
from national.data_extractor import nation_data
from .data_extractor import provinces_of_marche_data
from regions.data_extractor import extract_single_region_data
from dictionaries import area_codes
from dictionaries.area_names import area_names_dict as area_names
import utils

marche_data = extract_single_region_data(area_codes.marche)


def compute_total_cases_per_provinces(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces.
    """

    for province_code, province_data in provinces_of_marche_data.items():
        cases = utils.compute_x_days_mov_average(province_data['incr_casi_per_100000_ab'], 14)
        plt.plot(province_data['data'], cases, label=area_names[province_code])

    cases = utils.compute_x_days_mov_average(nation_data['nuovi_pos_per_100000_ab'], 14)
    plt.plot(nation_data['data'], cases, alpha=0.5, linestyle=':', label="Italia")

    cases = utils.compute_x_days_mov_average(marche_data['nuovi_pos_per_100000_ab'], 14)
    plt.plot(marche_data['data'], cases, alpha=0.5, linestyle=':', label="Marche")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Nuovi pos. ogni 100.000 ab. (14 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./assets/totale_casi_per_province_marche.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_total_cases_per_provinces_abs(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces, as absolute cases.
    """

    cases_stack = []
    labels = []
    dates = []
    for province_code, province_data in provinces_of_marche_data.items():
        cases = utils.compute_x_days_mov_average(province_data['incremento_casi'], 14)
        cases_stack.append(cases)
        labels.append(area_names[province_code])
        dates = province_data['data']

    plt.stackplot(dates, cases_stack, labels=labels)
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Nuovi pos. in val. ass. (14 gg. m.a.)')
    plt.legend(loc='upper left')

    if save_image:
        plt.savefig('./assets/totale_casi_per_province_marche_abs.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
