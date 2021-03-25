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


def compute_weekly_incidence(save_image=False, show=False):
    """
    Computes and plots the weekly positives incidence for some regions of interest. This is one
    of the indices used to determine the zone.
    """

    for province_code, province_data in provinces_of_marche_data.items():
        incidence = utils.compute_x_days_mov_average(province_data['incid_sett_per_100000_ab'], 7)
        plt.plot(province_data['data'], incidence, label=area_names[province_code])

    nat_incidence = utils.compute_x_days_mov_average(nation_data['incid_sett_per_100000_ab'], 7)
    plt.plot(nation_data['data'], nat_incidence, alpha=0.5, linestyle=':', label="Italia")

    marche_incidence = utils.compute_x_days_mov_average(marche_data['incid_sett_per_100000_ab'], 7)
    plt.plot(marche_data['data'], marche_incidence, alpha=0.5, linestyle=':', label="Marche")

    plt.axhline(y=250, color='tab:red', linestyle='--', alpha=0.5, label="Alto rischio")
    plt.axhline(y=50, color='tab:orange', linestyle='--', alpha=0.5, label="Basso rischio")

    plt.gca().set_ylim([0, None])
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Incid. sett. pos. per 100.000 ab. (7 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./assets/incid_sett_marche.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
