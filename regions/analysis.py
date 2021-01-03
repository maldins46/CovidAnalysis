#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid.
@author: riccardomaldini
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from . import regions_names as reg
from .data_extractor import benchmark_regions_data, extract_single_region_data
from national.data_extractor import nation_data


def compute_ti_occupation_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones, for some regions of interest.
    """

    for region_name, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data'], region_data['occupazione_ti'], label=region_name)

    plt.plot(nation_data['data'], nation_data['occupazione_ti'], alpha=0.5, linestyle=':', label="Italia")

    plt.axhline(y=0.3, color='y', linestyle='--', alpha=0.5, label="Livello d'allerta")
    plt.axhline(y=1, color='r', linestyle='--', alpha=0.5, label="Saturazione")

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Occupazione TI')
    plt.ylabel('Percentuale occupaz. TI')
    plt.legend()

    if save_image:
        plt.savefig('./docs/ti_per_regioni.png', dpi=300, transparent=True)

    if show:
        plt.show()

    plt.close()


def compute_positivity_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between tests and positive ones, for some regions of interest.
    """

    for region_name, region_data in benchmark_regions_data.items():
        dates, pos = compute_x_days_mov_average(region_data, 'tasso_positivita', 14)
        plt.plot(dates, pos, label=region_name)

    dates, pos = compute_x_days_mov_average(nation_data, 'tasso_positivita', 14)
    plt.plot(dates, pos, alpha=0.5, linestyle=':', label="Italia")

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Tasso di positività')
    plt.ylabel('Tamp. pos. su effettuati (7 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/positivita.png', dpi=300, transparent=True)

    if show:
        plt.show()

    plt.close()


def compute_rec_with_symptoms(save_image=False, show=False):
    """
    Computes and plots recovered with symptoms.
    """

    for region_name, region_data in benchmark_regions_data.items():
        plt.plot(region_data['data'], region_data['ric_per_100000_ab'], label=region_name)

    plt.plot(nation_data['data'], nation_data['ric_per_100000_ab'], alpha=0.5, linestyle=':', label="Italia")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Ricoverati con sintomi')
    plt.ylabel('Ric. con sintomi ogni 100.000 abitanti')
    plt.legend()

    if save_image:
        plt.savefig('./docs/ricoverati_con_sintomi_per_regioni.png', dpi=300, transparent=True)

    if show:
        plt.show()

    plt.close()


def compute_daily_cases(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones, for some regions of interest.
    """

    for region_name, region_data in benchmark_regions_data.items():
        dates, pos = compute_x_days_mov_average(region_data, 'nuovi_pos_per_100000_ab', 7)
        plt.plot(dates, pos, label=region_name)

    dates, pos = compute_x_days_mov_average(nation_data, 'nuovi_pos_per_100000_ab', 7)
    plt.plot(dates, pos, alpha=0.5, linestyle=':', label="Italia")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Nuovi positivi')
    plt.ylabel('Nuovi pos. ogni 100.000 ab. (7 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/positivi_per_regioni.png', dpi=300, transparent=True)

    if show:
        plt.show()

    plt.close()


def compute_death(save_image=False, show=False):
    """
    Computes and plots daily deaths.
    """

    for region_name, region_data in benchmark_regions_data.items():
        dates, deaths = compute_x_days_mov_average(region_data, 'incr_morti_per_100000_ab', 7)
        plt.plot(dates, deaths, label=region_name)

    dates, deaths = compute_x_days_mov_average(nation_data, 'incr_morti_per_100000_ab', 7)
    plt.plot(dates, deaths, alpha=0.5, linestyle=':', label="Italia")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Deceduti')
    plt.xlabel('Date')
    plt.ylabel('Dec. ogni 100.000 ab. (7 gg. m.a.)')
    plt.legend()

    if save_image:
        plt.savefig('./docs/deceduti_per_regioni.png', dpi=300, transparent=True)

    if show:
        plt.show()

    plt.close()


def compute_region_parameters(save_image=False, show=False, region_name=reg.marche):
    """
    Different data about region Marche.
    """

    region_df = extract_single_region_data(region_name)

    dates, deaths = compute_x_days_mov_average(region_df, 'incremento_morti', 7)
    plt.plot(dates, deaths, label='Incremento morti (7 gg. m.a.)')

    plt.plot(region_df['data'], region_df['terapia_intensiva'], label='Pazienti TI')

    dates, pos = compute_x_days_mov_average(region_df, 'nuovi_positivi', 7)
    plt.plot(dates, pos, label="Nuovi positivi (7 gg. m.a.)")

    plt.plot(region_df['data'], region_df['ricoverati_con_sintomi'], label="Ricoverati con sintomi")

    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title(f"Parametri  COVID-19 {region_name}")
    plt.ylabel('Variaz. parametri')
    plt.legend()

    if save_image:
        plt.savefig(f"./docs/parametri_{region_name.lower().replace(' ', '_')}", dpi=300, transparent=True)

    if show:
        plt.show()

    plt.close()


def compute_x_days_mov_average(df, column, window=7):
    """
    Computes an x-days-moving-average on the given column, of the given
    dataframe, and returns the computed column and the correspondant dates,
    for plotting.
    """

    column_ma = np.convolve(df[column], np.ones(window)/window, mode='valid')
    dates = df.iloc[window-1:].data

    return dates, column_ma
