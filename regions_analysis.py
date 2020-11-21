#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with useful elaborations about italian covid.
@author: riccardomaldini
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import dateutil.parser as datePrs
import regions_denomination as reg
from ti_places import ti_places_dict as ti_places


def extract_regions_data(path = './GvtOpenData/dati-regioni'):
    """ Reads all csv files about regions data and concatenates them in a
    data frame."""
    
    all_files_paths = os.path.join(path, "*.csv")
    all_files = glob.glob(all_files_paths)
    return pd.concat((pd.read_csv(file) for file in all_files))


# Create dataframe, extract some region data, plot all available 
# info into files inside docs directory
df = extract_regions_data()


def extract_single_region_data(region):
    """ 
    Extracts all data about a single region, it sort them, and adds.
    additional data about TI occupation, if available. Also, converts dates 
    to datetime. 
    """
    
    region_df = df.loc[df['denominazione_regione'] == region]
    
    # Adds TI occupation data
    region_df = region_df.assign(occupazione_ti=pd.Series(np.zeros(region_df.size)))
    for index, row in region_df.iterrows():
        region_df.at[index, 'occupazione_ti'] = row['terapia_intensiva'] / ti_places[row['denominazione_regione']]
        region_df.at[index, 'data'] = datePrs.parse(row['data'])
        
    region_df = region_df.sort_values('data')

    # Remove some problematic data
    return region_df[~region_df.index.duplicated(keep=False)]


def extract_regions_of_interest():
    """
    Extract some regions defined as of interest in the analysis, as a dictionary.
    """
    return {
        reg.lombardia: extract_single_region_data(reg.lombardia),
        reg.emilia_romagna: extract_single_region_data(reg.emilia_romagna),
        reg.molise: extract_single_region_data(reg.molise),
        reg.marche: extract_single_region_data(reg.marche)
    }


def compute_ti_occupation_per_regions(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones,
    for some regions of interest. 
    """

    regions = extract_regions_of_interest()
    
    for region_name, region in regions.items():
        plt.plot(region['data'], region['occupazione_ti'], label=region_name)
    
    plt.axhline(y=0.3, color='r', linestyle='--', label="Livello d'allerta")
    plt.axhline(y=1, color='y', linestyle='--', label="Saturazione")
    
    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Occupazione TI giornaliera per regioni')
    plt.xlabel('Date')
    plt.ylabel('Occupazione TI giornaliera')
    plt.legend()
    
    if save_image:
        plt.savefig('./docs/ti_per_regioni.png', dpi=300)
    
    if show:
        plt.show()
    
    plt.close()
    

def compute_rec_with_symptoms(save_image=False, show=False):
    """
    Computes and plots recovered with symptoms. 
    """

    regions = extract_regions_of_interest()
    
    for region_name, region in regions.items():
        plt.plot(region['data'], region['ricoverati_con_sintomi'], label=region_name)
    
    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Ricoverati con sintomi giornalieri per regioni')
    plt.xlabel('Date')
    plt.ylabel('Ricoverati con sintomi')
    plt.legend()
    
    if save_image:
        plt.savefig('./docs/ricoverati_con_sintomi_per_regioni.png', dpi=300)
    
    if show:
        plt.show()

    plt.close()
    
    
def compute_daily_cases(save_image=False, show=False):
    """
    Computes and plots relations between occupied TI places and available ones,
    for some regions of interest. 
    """
    
    regions = extract_regions_of_interest()
    
    for region_name, region in regions.items():
        plt.plot(region['data'], region['nuovi_positivi'], label=region_name)
    
    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Nuovi positivi giornalieri per regione')
    plt.xlabel('Date')
    plt.ylabel('Nuovi positivi')
    plt.legend()
    
    if save_image:
        plt.savefig('./docs/positivi_per_regioni.png', dpi=300)
    
    if show:
        plt.show()

    plt.close()
  

def compute_death(save_image=False, show=False):
    """
    Computes and plots daily deaths. 
    """

    regions = extract_regions_of_interest()
    
    for region_name, region in regions.items():
        plt.plot(region['data'], region['deceduti'], label=region_name)
    
    plt.gcf().autofmt_xdate()
    plt.grid(True)
    plt.title('Deceduti giornalieri per regioni')
    plt.xlabel('Date')
    plt.ylabel('Deceduti')
    plt.legend()
    
    if save_image:
        plt.savefig('./docs/deceduti_per_regioni.png', dpi=300)
    
    if show:
        plt.show()

    plt.close()