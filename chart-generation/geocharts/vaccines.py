#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geographical charts about the vaccine campaign evolution.
@author: riccardomaldini
"""

from data_extractors.vaccines_regions import regions_geodf
import matplotlib.pyplot as plt


def adm_doses(save_image=False, show=False):
    regions_geodf['totale_su_pop_100'] = regions_geodf.apply(lambda x: x['totale_su_pop'] * 100, axis=1)
    regions_geodf['totale_su_pop_100_label'] = regions_geodf.apply(lambda x: f"{x['totale_su_pop_100']:.3f} %",
                                                                   axis=1)

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Percentuale della popolazione vaccinata\nnell\'ultimo giorno, per regione')

    for _, row in regions_geodf.iterrows():
        plt.annotate(text=row['totale_su_pop_100_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='totale_su_pop_100', legend=True, scheme="quantiles",
                       cmap='Blues', linewidth=0.6, edgecolor='0.6',
                       legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/vaccines/dosi_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def immunes_percentage(save_image=False, show=False):
    regions_geodf['seconda_dose_totale_storico_su_pop_100'] = regions_geodf.apply(lambda x: x['seconda_dose_totale_storico_su_pop'] * 100, axis=1)
    regions_geodf['seconda_dose_totale_storico_su_pop_label'] = regions_geodf.apply(lambda x: f"{x['seconda_dose_totale_storico_su_pop_100']:.2f} %",
                                                                                    axis=1)

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Percentuale popolazione immunizzata, per regione')

    for _, row in regions_geodf.iterrows():
        plt.annotate(text=row['seconda_dose_totale_storico_su_pop_label'], xy=row['coords'],
                     horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='seconda_dose_totale_storico_su_pop_100', legend=True, scheme="quantiles",
                       cmap='Blues', linewidth=0.6, edgecolor='0.6',
                       legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/vaccines/immunizzati_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def coverage_percentage(save_image=False, show=False):
    regions_geodf['prima_dose_totale_storico_su_pop_100'] = regions_geodf.apply(lambda x: x['prima_dose_totale_storico_su_pop'] * 100, axis=1)
    regions_geodf['prima_dose_totale_storico_su_pop_label'] = regions_geodf.apply(lambda x: f"{x['prima_dose_totale_storico_su_pop_100']:.2f} %",
                                                                                  axis=1)

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.axis('off')

    plt.title('Percentuale popolazione coperta da\nalmeno una dose, per regione')

    for _, row in regions_geodf.iterrows():
        plt.annotate(text=row['prima_dose_totale_storico_su_pop_label'], xy=row['coords'],
                     horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='prima_dose_totale_storico_su_pop_100', legend=True, scheme="quantiles",
                       cmap='Blues', linewidth=0.6, edgecolor='0.6',
                       legend_kwds=dict(loc='upper right', frameon=False))

    if save_image:
        fig.savefig('./charts/vaccines/copertura_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
