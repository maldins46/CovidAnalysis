#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Charts about the epidemiologial evolution through time at Marche regional/provincial level.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator
from data_extractors.covid_italy import italy_df
from data_extractors.covid_regions import marche_df
from data_extractors.covid_provinces import marche_dict
from data_extractors.area_names import area_names_dict
import utils


def parameters(save_image=False, show=False):
    """
    Summary of different historical data about Marche, in absolute numbers.
    """

    deaths = utils.compute_x_days_mov_average(marche_df['incremento_morti'], 7)
    plt.plot(marche_df['data'], deaths, label='Nuovi decessi (7 gg. m.a.)')

    plt.plot(marche_df['data'], marche_df['terapia_intensiva'], label='Pazienti TI')

    pos = marche_df['nuovi_positivi'].rolling(7).mean()
    plt.plot(marche_df['data'], pos, label="Nuovi positivi (7 gg. m.a.)")

    plt.plot(marche_df['data'], marche_df['ricoverati_con_sintomi'], label="Ricoverati con sintomi")

    plt.title('Evoluzione parametri Marche, in valori assoluti')
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Variaz. parametri')
    plt.legend()

    if save_image:
        plt.savefig(f"./assets/parametri_marche", dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()

def cases_per_provinces_abs(save_image=False, show=False):
    """
    Computes and plots total cases in Marche provinces, as absolute cases.
    """

    cases_stack = []
    labels = []
    dates = []
    for province_code, province_data in marche_dict.items():
        cases = province_data['nuovi_positivi'].rolling(14, center=True).mean()
        cases_stack.append(cases)
        labels.append(area_names_dict[province_code])
        dates = province_data['data']

    plt.title('Nuovi positivi nelle Marche')
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


def weekly_incidence(save_image=False, show=False):
    """
    Computes and plots the weekly positives incidence for some regions of interest. This is one
    of the indices used to determine the zone.
    """

    for province_code, province_data in marche_dict.items():
        incidence = province_data['incid_sett_per_100000_ab'].rolling(7, center=True).mean()
        plt.plot(province_data['data'], incidence, label=area_names_dict[province_code])

    nat_incidence = utils.compute_x_days_mov_average(italy_df['incid_sett_per_100000_ab'], 7)
    plt.plot(italy_df['data'], nat_incidence, alpha=0.5, linestyle=':', label="Italia")

    marche_incidence = marche_df['incid_sett_per_100000_ab'].rolling(7, center=True).mean()
    plt.plot(marche_df['data'], marche_incidence, alpha=0.5, linestyle=':', label="Marche")

    plt.axhline(y=250, color='tab:red', linestyle='--', alpha=0.5, label="Alto rischio")
    plt.axhline(y=50, color='tab:orange', linestyle='--', alpha=0.5, label="Basso rischio")

    plt.title('Incidenza sett. nuovi pos. Marche per 100.000 abitanti')
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
