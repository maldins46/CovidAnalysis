#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geographical charts about the epidemiologial evolution.
@author: riccardomaldini
"""

from data_extractors.covid_regions import regions_geodf
from data_extractors.covid_provinces import provinces_geodf
import pandas as pd
import matplotlib.pyplot as plt


def ti_occupation(save_image=False, show=False):
    """
    Geographical chart that shows relations between occupied TI places and available ones,
    for all regions of Italy.
    """

    regions_geodf['occupazione_ti_100'] = regions_geodf['occupazione_ti'].apply(lambda x: x * 100)
    regions_geodf['occupazione_ti_label'] = regions_geodf['occupazione_ti_100'].apply(lambda x: f"{x:.2f}%")

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Occupazione terapie intensive, per regione')

    for _, row in regions_geodf.iterrows():
        plt.annotate(text=row['occupazione_ti_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='occupazione_ti_100', legend=True, scheme="equal_interval",
                       cmap='OrRd', linewidth=0.6, edgecolor='0.6',
                       legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/ti_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_increment_ti(save_image=False, show=False):
    """
    Geographical chart that shows the increment of TI pressure,
    for all regions of Italy.
    """

    regions_geodf['incremento_incidenza_ti_100'] = regions_geodf['incremento_incidenza_ti'].apply(lambda x: x * 100)
    regions_geodf['incremento_incidenza_ti_label'] = regions_geodf['incremento_incidenza_ti_100'].apply(lambda x: f"{x:.2f}%" if x <= 0 else f"+{x:.2f}%")

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incremento/decremento occupazione terapie\nintensive rispetto alla settimana precedente, per regione')

    for _, row in regions_geodf.iterrows():
        plt.annotate(text=row['incremento_incidenza_ti_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    pos = regions_geodf[regions_geodf['incremento_incidenza_ti_100'] >= 0]
    base = pos.plot(ax=ax, column='incremento_incidenza_ti_100', legend=False, scheme="quantiles",
                    cmap='Oranges', linewidth=0.6, edgecolor='0.6')

    neg = regions_geodf[regions_geodf['incremento_incidenza_ti_100'] < 0]

    pd.options.mode.chained_assignment = None
    neg['incremento_incidenza_ti_100'] = neg['incremento_incidenza_ti_100'].apply(lambda x: -x)
    pd.options.mode.chained_assignment = 'warn'

    neg.plot(ax=base, column='incremento_incidenza_ti_100', legend=False, scheme="quantiles",
             cmap='Greens', linewidth=0.6, edgecolor='0.6')

    if save_image:
        fig.savefig('./charts/covid/increm_sett_ti_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_incidence_regions(save_image=False, show=False):
    """
    Geographical chart that shows the weekly positives incidence,
    for all regions of Italy.
    """

    regions_geodf['incid_sett_per_100000_round'] = regions_geodf['incid_sett_per_100000_ab'].apply(lambda x: round(x, 0))
    regions_geodf['incid_sett_per_100000_ab_label'] = regions_geodf['incid_sett_per_100000_round'].apply(lambda x: f"{x:.0f}")

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incidenza settimanale nuovi positivi\nper 100.000 abitanti, per regione')

    for _, row in regions_geodf.iterrows():
        plt.annotate(text=row['incid_sett_per_100000_ab_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='incid_sett_per_100000_round', legend=True, scheme="equal_interval",
                       cmap='OrRd', linewidth=0.6, edgecolor='0.6',
                       legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/incidenza_sett_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_increment_regions(save_image=False, show=False):
    """
    Geographical chart that shows the increment of the incidence,
    for all regions of Italy.
    """

    regions_geodf['incremento_incidenza_100'] = regions_geodf['incremento_incidenza'].apply(lambda x: x * 100)
    regions_geodf['incremento_incidenza_label'] = regions_geodf['incremento_incidenza_100'].apply(lambda x: f"{x:.2f}%" if x <= 0 else f"+{x:.2f}%")

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incremento/decremento casi rispetto alla\nsettimana precedente, per regione')

    for _, row in regions_geodf.iterrows():
        plt.annotate(text=row['incremento_incidenza_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    pos = regions_geodf[regions_geodf['incremento_incidenza_100'] >= 0]
    base = pos.plot(ax=ax, column='incremento_incidenza_100', legend=False, scheme="quantiles",
                    cmap='Oranges', linewidth=0.6, edgecolor='0.6')

    neg = regions_geodf[regions_geodf['incremento_incidenza_100'] < 0]

    pd.options.mode.chained_assignment = None
    neg['incremento_incidenza_100'] = neg['incremento_incidenza_100'].apply(lambda x: -x)
    pd.options.mode.chained_assignment = 'warn'

    neg.plot(ax=base, column='incremento_incidenza_100', legend=False, scheme="quantiles",
             cmap='Greens', linewidth=0.6, edgecolor='0.6')

    if save_image:
        fig.savefig('./charts/covid/increm_sett_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_incidence_provinces(save_image=False, show=False):
    """
    Geographical chart that shows the weekly positives incidence,
    for all provinces of Italy.
    """

    provinces_geodf['incid_sett_100000_round'] = provinces_geodf['incid_sett_per_100000_ab'].apply(lambda x: round(x, 0))
    provinces_geodf['incid_sett_100000_ab_label'] = provinces_geodf['incid_sett_100000_round'].apply(lambda x: f"{x:.0f}")

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incidenza settimanale nuovi positivi\nper 100.000 abitanti, per provincia')

    for _, row in provinces_geodf.iterrows():
        plt.annotate(text=row['incid_sett_100000_ab_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    provinces_geodf.plot(ax=ax, column='incid_sett_100000_round', legend=True,
                         cmap='OrRd', linewidth=0.6, edgecolor='0.6',
                         legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/incidenza_sett_per_prov_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_increment_provinces(save_image=False, show=False):
    """
    Geographical chart that shows the increment of the incidence,
    for all provinces of Italy.
    """

    provinces_geodf['incremento_incidenza_100'] = provinces_geodf['incremento_incidenza'].apply(lambda x: x * 100)
    provinces_geodf['incremento_incidenza_label'] = provinces_geodf['incremento_incidenza_100'].apply(lambda x: f"{x:.0f}%" if x <= 0 else f"+{x:.0f}%")

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incremento/decremento casi rispetto alla\nsettimana precedente, per provincia')

    for _, row in provinces_geodf.iterrows():
        plt.annotate(text=row['incremento_incidenza_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    pos = provinces_geodf[provinces_geodf['incremento_incidenza_100'] >= 0]
    base = pos.plot(ax=ax, column='incremento_incidenza_100', legend=False, scheme="quantiles",
                    cmap='Oranges', linewidth=0.6, edgecolor='0.6')

    neg = provinces_geodf[provinces_geodf['incremento_incidenza_100'] < 0]

    pd.options.mode.chained_assignment = None
    neg['incremento_incidenza_100'] = neg['incremento_incidenza_100'].apply(lambda x: -x)
    pd.options.mode.chained_assignment = 'warn'

    neg.plot(ax=base, column='incremento_incidenza_100', legend=False, scheme="quantiles",
             cmap='Greens', linewidth=0.6, edgecolor='0.6')

    if save_image:
        fig.savefig('./charts/covid/increm_sett_per_provincia_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
