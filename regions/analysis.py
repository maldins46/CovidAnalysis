#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.dates import MonthLocator, DateFormatter
from dictionaries import area_codes as areas
from dictionaries.area_names import area_names_dict as area_names
from .data_extractor import benchmark_regions_data, extract_single_region_data
from national.data_extractor import nation_data
import utils


def compute_ti_occupation_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones, for some regions of interest.
    """

    for region_code, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data'], region_data['occupazione_ti'], label=area_names[region_code])

    plt.plot(nation_data['data'], nation_data['occupazione_ti'], alpha=0.5, linestyle=':', label="Italia")

    plt.axhline(y=0.3, color='y', linestyle='--', alpha=0.5, label="Livello d'allerta")
    plt.axhline(y=1, color='r', linestyle='--', alpha=0.5, label="Saturazione")

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Percentuale occupaz. TI')
    plt.legend()

    if save_image:
        plt.savefig('./docs/ti_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_rt_per_regions(save_image=False, show=False):
    """
    Computes and plots RT for some regions of interest, with SIRD model applied as by INFN.
    https://covid19.infn.it/banner/Approfondimenti.pdf
    """

    for region_code, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data'], region_data['rt'], label=area_names[region_code])

    plt.plot(nation_data['data'], nation_data['rt'], alpha=0.5, linestyle=':', label="Italia")

    plt.axhline(y=1.50, color='tab:red', linestyle='--', alpha=0.5, label="Scenario 4")
    plt.axhline(y=1.25, color='tab:orange', linestyle='--', alpha=0.5, label="Scenario 3")
    plt.axhline(y=1, color='y', linestyle='--', alpha=0.5, label="Scenario 2")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Indice RT (4 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/rt_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_weekly_incidence(save_image=False, show=False):
    """
    Computes and plots the weekly positives incidence for some regions of interest. This is one
    of the indices used to determine the zone.
    """

    for region_code, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data'], region_data['incid_sett_per_100000_ab'], label=area_names[region_code])

    plt.plot(nation_data['data'], nation_data['incid_sett_per_100000_ab'], alpha=0.5, linestyle=':', label="Italia")

    plt.axhline(y=50, color='tab:orange', linestyle='--', alpha=0.5, label="Soglia incidenza")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Incid. sett. pos. per 100.000 ab.')
    plt.legend()

    if save_image:
        plt.savefig('./docs/incid_sett_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_positivity_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between tests and positive ones, for some regions of interest.
    """

    for region_code, region_data in benchmark_regions_data.items():
        pos = utils.compute_x_days_mov_average(region_data['tasso_positivita'], 14)
        plt.plot(region_data['data'], pos, label=area_names[region_code])

    pos = utils.compute_x_days_mov_average(nation_data['tasso_positivita'], 14)
    plt.plot(nation_data['data'], pos, alpha=0.5, linestyle=':', label="Italia")

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Tamp. pos. su effettuati (14 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/positivita.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_rec_with_symptoms(save_image=False, show=False):
    """
    Computes and plots recovered with symptoms.
    """

    for region_code, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data'], region_data['ric_per_100000_ab'], label=area_names[region_code])

    plt.plot(nation_data['data'], nation_data['ric_per_100000_ab'], alpha=0.5, linestyle=':', label="Italia")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Ric. con sintomi ogni 100.000 abitanti')
    plt.legend()

    if save_image:
        plt.savefig('./docs/ricoverati_con_sintomi_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_daily_cases(save_image=False, show=False):
    """
    Computes daily cases, for some regions of interest.
    """

    for region_code, region_data in benchmark_regions_data.items():
        pos = utils.compute_x_days_mov_average(region_data['nuovi_pos_per_100000_ab'], 7)
        plt.plot(region_data['data'], pos, label=area_names[region_code])

    pos = utils.compute_x_days_mov_average(nation_data['nuovi_pos_per_100000_ab'], 7)
    plt.plot(nation_data['data'], pos, alpha=0.5, linestyle=':', label="Italia")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Nuovi pos. ogni 100.000 ab. (7 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/positivi_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_death(save_image=False, show=False):
    """
    Computes and plots daily deaths.
    """

    for region_code, region_data in benchmark_regions_data.items():
        deaths = utils.compute_x_days_mov_average(region_data['incr_morti_per_100000_ab'], 7)
        plt.plot(region_data['data'], deaths, label=area_names[region_code])

    deaths = utils.compute_x_days_mov_average(nation_data['incr_morti_per_100000_ab'], 7)
    plt.plot(nation_data['data'], deaths, alpha=0.5, linestyle=':', label="Italia")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Dec. ogni 100.000 ab. (7 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/deceduti_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_region_parameters(save_image=False, show=False, region_code=areas.marche):
    """
    Different data about a single region.
    """

    region_data = extract_single_region_data(region_code)

    deaths = utils.compute_x_days_mov_average(region_data['incremento_morti'], 7)
    plt.plot(region_data['data'], deaths, label='Nuovi decessi (7 gg. m.a.)')

    plt.plot(region_data['data'], region_data['terapia_intensiva'], label='Pazienti TI')

    pos = utils.compute_x_days_mov_average(region_data['nuovi_positivi'], 7)
    plt.plot(region_data['data'], pos, label="Nuovi positivi (7 gg. m.a.)")

    plt.plot(region_data['data'], region_data['ricoverati_con_sintomi'], label="Ricoverati con sintomi")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gca().xaxis.set_minor_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Variaz. parametri')
    plt.legend()

    if save_image:
        region_name_clean = area_names[region_code].lower().replace(' ', '_')
        plt.savefig(f"./docs/parametri_{region_name_clean}", dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
