#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geographical charts about the vaccine campaign evolution.
@author: riccardomaldini
"""

import sys
import geopandas as gpd
import pandas as pd
from data_extractors.vaccines_regions import regions_geodf
import matplotlib.pyplot as plt


def adm_doses(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    plt.title('Dosi somministrate nell\'ultimo giorno')

    # Display names 
    for idx, row in regions_geodf.iterrows():
        plt.annotate(text=row['totale'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='totale', legend=True, scheme="quantiles", 
                    cmap='Blues', linewidth=0.6, edgecolor='0.6',
                    legend_kwds=dict(loc='upper right', title="Somministraz. ultimo giorno\n", frameon=False))

    if save_image:
        fig.savefig('./assets/dosi_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def immunes_percentage(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    plt.title('Percentuale popolazione immunizzata')


    # Display names 
    for idx, row in regions_geodf.iterrows():
        plt.annotate(text=row['seconda_dose_totale_storico_su_pop_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    regions_geodf.plot(ax=ax, column='seconda_dose_totale_storico_su_pop_100', legend=True, scheme="quantiles", 
                    cmap='Blues', linewidth=0.6, edgecolor='0.6',
                    legend_kwds=dict(loc='upper right', title="% popolaz. immunizzata\n", frameon=False))

    if save_image:
        fig.savefig('./assets/immunizzati_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
