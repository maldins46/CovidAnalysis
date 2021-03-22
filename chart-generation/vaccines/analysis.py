#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analysis on the national vaccine data.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from dictionaries.area_names import area_names_dict as area_names
from dictionaries import area_codes as areas
from .data_extractor import benchmark_regions_data, extract_area_adm_data
from .data_extractor import nation_data
from matplotlib.dates import MonthLocator
import utils


def compute_adm(save_image=False, show=False, area_code=areas.italia):
    """
    Administration data about Italy.
    """
    data = extract_area_adm_data(area_code) if area_code != areas.italia else nation_data

    # plt.stackplot(data['data_somministrazione'], data['prima_dose'],data['seconda_dose'],
    #               labels=['Prime dosi', 'Seconde dosi'])
    plt.bar(data['data_somministrazione'], data['prima_dose'], label='Prime dosi')
    plt.bar(data['data_somministrazione'], data['seconda_dose'], bottom=data['prima_dose'],
            label='Seconde dosi')

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')

    plt.ylabel('Somministraz. giornaliere')
    plt.legend()

    if save_image:
        area_name_clean = area_names[area_code].lower().replace(' ', '_')
        plt.savefig(f'./assets/dosi_{area_name_clean}.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_regional_doses(save_image=False, show=False):
    """
    Comparation between doses administrated in various regions
    """

    for area_code, region_data in benchmark_regions_data.items():
        rolling_avg_adm = region_data['totale_per_100000_ab'].rolling(7, center=True).mean()
        plt.plot(region_data['data_somministrazione'], rolling_avg_adm, label=area_names[area_code])

    rolling_avg_adm = nation_data['totale_per_100000_ab'].rolling(7, center=True).mean()
    plt.plot(nation_data['data_somministrazione'], rolling_avg_adm, alpha=0.5, linestyle=':',
             label="Italia")

    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Somministraz. ogni 100.000 abitanti (7 gg. m.a.')
    plt.legend()

    if save_image:
        plt.savefig('./assets/dosi_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_immunes_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between the population of a place and people that took the second shot.
    """

    for area_code, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data_somministrazione'], region_data['acc_perc_seconda_dose'], label=area_names[area_code])

    plt.plot(nation_data['data_somministrazione'], nation_data['acc_perc_seconda_dose'], alpha=0.5, linestyle=':',
             label="Italia")

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    plt.gca().xaxis.set_major_formatter(utils.std_date_formatter)
    plt.gca().xaxis.set_minor_formatter(utils.std_date_formatter)
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Percentuale popolaz. immunizz.')
    plt.legend()

    if save_image:
        plt.savefig('./assets/immunizzati.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
