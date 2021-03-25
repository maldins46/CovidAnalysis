import sys
import geopandas as gpd
import pandas as pd
from .data_extractor import extract_map_data
import matplotlib.pyplot as plt

regions_geo_df = extract_map_data()


def compute_ti_map(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    regions_geo_df['occupazione_ti_100'] = regions_geo_df.apply(lambda x: x['occupazione_ti'] * 100, axis=1)
    regions_geo_df['occupazione_ti_label'] = regions_geo_df.apply(lambda x: f"{x['occupazione_ti_100']:.2f} %", axis=1)

    # Add location for the labels
    regions_geo_df['coords'] = regions_geo_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    regions_geo_df['coords'] = [coords[0] for coords in regions_geo_df['coords']]

    # Display names 
    for idx, row in regions_geo_df.iterrows():
        plt.annotate(text=row['occupazione_ti_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    regions_geo_df.plot(ax=ax, column='occupazione_ti_100', legend=True, scheme="user_defined", 
                    cmap='OrRd', linewidth=0.6, edgecolor='0.6',classification_kwds={'bins':[5,10, 30, 50]},
                    legend_kwds=dict(loc='upper right', title="Occupazione TI\n", frameon=False))

    if save_image:
        fig.savefig('./assets/ti_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()


def compute_incidence_map(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    # Add location for the labels
    regions_geo_df['coords'] = regions_geo_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    regions_geo_df['coords'] = [coords[0] for coords in regions_geo_df['coords']]

    # Round data for better readability
    regions_geo_df['incid_sett_per_100000'] = regions_geo_df.apply(lambda x: round(x['incid_sett_per_100000_ab'], 0), axis=1)
    regions_geo_df['incid_sett_per_100000_ab_label'] = regions_geo_df.apply(lambda x: f"{x['incid_sett_per_100000_ab']:.0f}", axis=1)

    # custom cmap:
    #from matplotlib.colors import ListedColormap
    #cmap = ListedColormap(["green", "orange", "red", "black"])

    # Display names 
    for idx, row in regions_geo_df.iterrows():
        plt.annotate(text=row['incid_sett_per_100000_ab_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    regions_geo_df.plot(ax=ax, column='incid_sett_per_100000', legend=True, scheme="user_defined", 
                    cmap='OrRd', linewidth=0.6, edgecolor='0.6', classification_kwds={'bins':[50, 100, 250, 350]},
                    legend_kwds=dict(loc='upper right', title="Incid.sett. per 100.000 ab.\n", frameon=False))

    if save_image:
        fig.savefig('./assets/incidenza_sett_per_regioni_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()