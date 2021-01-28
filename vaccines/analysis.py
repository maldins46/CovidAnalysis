#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analysis on the national vaccine data.
@author: riccardomaldini
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.dates import DateFormatter, DayLocator
from .areas_name import areas_name_dict as areas_name
from . import areas
from .data_extractor import benchmark_regions_data, extract_area_adm_data
from .data_extractor import nation_data


def compute_adm(save_image=False, show=False, area_code=areas.italia):
    """
    Administration data about Italy.
    """
    data = extract_area_adm_data(area_code)

    # plt.stackplot(data['data_somministrazione'], data['prima_dose'],data['seconda_dose'],
    #               labels=['Prime dosi', 'Seconde dosi'])
    plt.bar(data['data_somministrazione'], data['prima_dose'], label='Prime dosi')
    plt.bar(data['data_somministrazione'], data['seconda_dose'], bottom=data['prima_dose'],
            label='Seconde dosi')

    plt.gca().xaxis.set_major_locator(DayLocator(interval=2))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')

    plt.ylabel('Somministraz. giornaliere')
    plt.legend()

    if save_image:
        area_name_clean = areas_name[area_code].lower().replace(' ', '_')
        plt.savefig(f'./docs/dosi_{area_name_clean}.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_regional_doses(save_image=False, show=False):
    """
    Comparation between doses administrated in various regions
    """

    for area_code, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data_somministrazione'], region_data['totale_per_100000_ab'], label=areas_name[area_code])

    plt.plot(nation_data['data_somministrazione'], nation_data['totale_per_100000_ab'], alpha=0.5, linestyle=':',
             label="Italia")

    plt.gca().xaxis.set_major_locator(DayLocator(interval=2))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Somministraz. ogni 100.000 abitanti')
    plt.legend()

    if save_image:
        plt.savefig('./docs/dosi_per_regioni.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_immunes_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between the population of a place and people that took the second shot.
    """

    for area_code, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data_somministrazione'], region_data['acc_perc_seconda_dose'], label=areas_name[area_code])

    plt.plot(nation_data['data_somministrazione'], nation_data['acc_perc_seconda_dose'], alpha=0.5, linestyle=':',
             label="Italia")

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    plt.gca().xaxis.set_major_locator(DayLocator(interval=2))
    plt.gca().xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.gcf().autofmt_xdate(which='both')
    plt.grid(True, which='both', axis='both')
    plt.ylabel('Percentuale popolaz. immunizz.')
    plt.legend()

    if save_image:
        plt.savefig('./docs/immunizzati.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
