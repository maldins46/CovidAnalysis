#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geographical charts about the epidemiologial evolution.
@author: riccardomaldini
"""

from data_extractors.covid_regions import regions_geodf
from data_extractors.covid_provinces import provinces_geodf
import matplotlib.pyplot as plt


def ti_occupation(save_image=False, show=False):
    """
    Geographical chart that shows relations between occupied TI places and available ones,
    for all regions of Italy.
    """

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Occupazione terapie intensive, per regione')

    for row in regions_geodf.itertuples(index=True, name='Pandas'):
        plt.annotate(text=row.occupazione_ti_label, xy=row.coords, horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='occupazione_ti_100', legend=True, scheme="user_defined",
                       cmap='OrRd', linewidth=0.6, edgecolor='0.6', classification_kwds={'bins': [5, 10, 30, 50]},
                       legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/ti_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_incidence_regions(save_image=False, show=False):
    """
    Geographical chart that shows the weekly positives incidence,
    for all regions of Italy.
    """

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incidenza settimanale nuovi positivi\nper 100.000 abitanti, per regione')

    for row in regions_geodf.itertuples(index=True, name='Pandas'):
        plt.annotate(text=row.incid_sett_per_100000_ab_label, xy=row.coords, horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='incid_sett_per_100000_round', legend=True, scheme="user_defined",
                       cmap='OrRd', linewidth=0.6, edgecolor='0.6', classification_kwds={'bins': [50, 100, 250, 350]},
                       legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/incidenza_sett_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def weekly_incidence_provinces(save_image=False, show=False):
    """
    Geographical chart that shows the weekly positives incidence,
    for all provinces of Italy.
    """

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Incidenza settimanale nuovi positivi\nper 100.000 abitanti, per provincia')

    for row in provinces_geodf.itertuples(index=True, name='Pandas'):
        plt.annotate(text=row.incid_sett_per_100000_ab_label, xy=row.coords, horizontalalignment='center', fontsize=10)

    provinces_geodf.plot(ax=ax, column='incid_sett_per_100000_round', legend=True, scheme="user_defined",
                         cmap='OrRd', linewidth=0.6, edgecolor='0.6', classification_kwds={'bins': [50, 100, 250, 350]},
                         legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/covid/incidenza_sett_per_prov_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
