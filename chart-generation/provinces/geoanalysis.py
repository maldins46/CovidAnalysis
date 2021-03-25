import sys
import geopandas as gpd
import pandas as pd
from .data_extractor import extract_map_data
import matplotlib.pyplot as plt

provinces_geo_df = extract_map_data()


def compute_incidence_prov_map(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    # Add location for the labels
    provinces_geo_df['coords'] = provinces_geo_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    provinces_geo_df['coords'] = [coords[0] for coords in provinces_geo_df['coords']]

    # custom cmap:
    #from matplotlib.colors import ListedColormap
    #cmap = ListedColormap(["green", "orange", "red", "black"])

    # Display names 
    for idx, row in provinces_geo_df.iterrows():
        plt.annotate(text=row['incid_sett_per_100000_ab_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    provinces_geo_df.plot(ax=ax, column='incid_sett_per_100000', legend=True, scheme="user_defined", 
                    cmap='OrRd', linewidth=0.6, edgecolor='0.6', classification_kwds={'bins':[50, 100, 250, 350]},
                    legend_kwds=dict(loc='upper right', title="Incid.sett. per 100.000 ab.\n", frameon=False))

    if save_image:
        fig.savefig('./assets/incidenza_sett_per_prov_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()



def compute_incidence_marche_map(save_image=False, show=False):
    fig, ax = plt.subplots(1, figsize=(12,12))
    ax.axis('off')

    marche_df = provinces_geo_df[provinces_geo_df['reg_istat_code'] == '11']

    # Add location for the labels
    marche_df['coords'] = marche_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    marche_df['coords'] = [coords[0] for coords in marche_df['coords']]

    # Display names 
    for idx, row in marche_df.iterrows():
        plt.annotate(text=row['incid_sett_per_100000_ab_label'], xy=row['coords'], horizontalalignment='center', fontsize=10)

    marche_df.plot(ax=ax, column='incid_sett_per_100000', legend=True, scheme="user_defined", 
                    cmap='OrRd', linewidth=0.6, edgecolor='0.6', classification_kwds={'bins':[50, 100, 250, 350]},
                    legend_kwds=dict(loc='upper right', title="Incid.sett. per 100.000 ab.\n", frameon=False))

    if save_image:
        fig.savefig('./assets/incidenza_sett_marche_mappa.png', dpi=300, transparent=True, bbox_inches='tight')

    if show:
        plt.show()

    plt.close()
