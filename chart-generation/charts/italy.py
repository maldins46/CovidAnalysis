#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Charts about the epidemiologial evolution through time at national/regional level.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator
from data_extractors.covid_italy import italy_df
from data_extractors.covid_regions import benchmark_dict
from data_extractors.area_names import area_names_dict
import matplotlib.ticker as mtick
import utils


def parameters(save_image=False, show=False):
    """
    Summary of different historical data about Italy, in absolute numbers.
    """

    deaths = italy_df['incremento_morti'].rolling(7, center=True).mean()
    plt.plot(italy_df['data'], deaths, label='Nuovi decessi (7 gg. m.a.)')

    plt.plot(italy_df['data'], italy_df['terapia_intensiva'], label='Pazienti TI')

    pos = utils.compute_x_days_mov_average(italy_df['nuovi_positivi'], 7)
    plt.plot(italy_df['data'], pos, label="Nuovi positivi (7 gg. m.a.)")

    plt.plot(italy_df['data'], italy_df['ricoverati_con_sintomi'], label="Ricoverati con sintomi")

    plt.title('Evoluzione parametri nazionali, in valori assoluti')
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')

    plt.ylabel('Variaz. parametri')
    plt.legend()

    if save_image:
        plt.savefig('./charts/covid/parametri_italia.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def ti_occupation(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones, for some regions of interest.
    """

    for region_code, region_data in benchmark_dict.items():
        plt.plot(region_data['data'], region_data['occupazione_ti'], label=area_names_dict[region_code])

    plt.plot(italy_df['data'], italy_df['occupazione_ti'], alpha=0.5, linestyle=':', label="Italia")

    plt.axhline(y=0.3, color='y', linestyle='--', alpha=0.5, label="Livello d'allerta")
    plt.axhline(y=1, color='r', linestyle='--', alpha=0.5, label="Saturazione")

    plt.title('Occupazione terapie intensive')

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Percentuale occupaz. TI')
    plt.legend()

    if save_image:
        plt.savefig('./charts/covid/ti_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def rt_per_regions(save_image=False, show=False):
    """
    Computes and plots RT for some regions of interest, with SIRD model applied as by INFN.
    https://covid19.infn.it/banner/Approfondimenti.pdf
    """

    for region_code, region_data in benchmark_dict.items():
        rt = utils.compute_rt(region_data['totale_casi'], region_data['dimessi_guariti'], region_data['deceduti'])
        plt.plot(region_data['data'], rt, label=area_names_dict[region_code])

    plt.plot(italy_df['data'], italy_df['rt'], alpha=0.5, linestyle=':', label="Italia")

    plt.axhline(y=1.50, color='tab:red', linestyle='--', alpha=0.5, label="Scenario 4")
    plt.axhline(y=1.25, color='tab:orange', linestyle='--', alpha=0.5, label="Scenario 3")
    plt.axhline(y=1, color='y', linestyle='--', alpha=0.5, label="Scenario 2")

    plt.title('Indice R(t) SIRD')
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('R(t) SIRD (4 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./charts/covid/rt_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_incidence(save_image=False, show=False):
    """
    Computes and plots the weekly positives incidence for some regions of interest. This is one
    of the indices used to determine the zone.
    """

    for region_code, region_data in benchmark_dict.items():
        plt.plot(region_data['data'], region_data['incid_sett_per_100000_ab'], label=area_names_dict[region_code])

    plt.plot(italy_df['data'], italy_df['incid_sett_per_100000_ab'], alpha=0.5, linestyle=':', label="Italia")

    plt.axhline(y=250, color='tab:red', linestyle='--', alpha=0.5, label="Alto rischio")
    plt.axhline(y=50, color='tab:orange', linestyle='--', alpha=0.5, label="Basso rischio")

    plt.title('Incidenza settimanale nuovi positivi per 100.000 abitanti')
    plt.gca().set_ylim([0, 600])
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Incid. sett. pos. per 100.000 ab.')
    plt.legend()

    if save_image:
        plt.savefig('./charts/covid/incid_sett_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
