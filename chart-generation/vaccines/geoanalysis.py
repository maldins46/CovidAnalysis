import sys
import geopandas as gpd
import pandas as pd
from .data_extractor import extract_map_data
import matplotlib.pyplot as plt

vaccines_geo_df = extract_map_data()


def compute_adm_doses_map(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    # Add location for the labels
    vaccines_geo_df['coords'] = vaccines_geo_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    vaccines_geo_df['coords'] = [coords[0] for coords in vaccines_geo_df['coords']]

    # Display names 
    for idx, row in vaccines_geo_df.iterrows():
        plt.annotate(text=row['totale'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    vaccines_geo_df.plot(ax=ax, column='totale', legend=True, scheme="quantiles", 
                    cmap='Blues', linewidth=0.6, edgecolor='0.6',
                    legend_kwds=dict(loc='upper right', title="Somministraz. ultimo giorno\n", frameon=False))

    if save_image:
        fig.savefig('./assets/dosi_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_immunes_percentage_map(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    vaccines_geo_df['acc_perc_seconda_dose_100'] = vaccines_geo_df.apply(lambda x: x['acc_perc_seconda_dose'] * 100, axis=1)
    vaccines_geo_df['acc_perc_seconda_dose_label'] = vaccines_geo_df.apply(lambda x: f"{x['acc_perc_seconda_dose_100']:.2f} %", axis=1)

    # Add location for the labels
    vaccines_geo_df['coords'] = vaccines_geo_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    vaccines_geo_df['coords'] = [coords[0] for coords in vaccines_geo_df['coords']]

    # Display names 
    for idx, row in vaccines_geo_df.iterrows():
        plt.annotate(text=row['acc_perc_seconda_dose_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    vaccines_geo_df.plot(ax=ax, column='acc_perc_seconda_dose_100', legend=True, scheme="quantiles", 
                    cmap='Blues', linewidth=0.6, edgecolor='0.6',
                    legend_kwds=dict(loc='upper right', title="% popolaz. immunizzata\n", frameon=False))

    if save_image:
        fig.savefig('./assets/immunizzati_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
