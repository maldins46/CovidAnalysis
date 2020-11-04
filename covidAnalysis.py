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

# Intensive therapy available places. To be continued.
ti_places = {
    "Marche": 153,
    "Lombardia": 1260,
    "Molise": 27,
    "Campania": 600
}

def extract_regions_data(path = './GvtOpenData/dati-regioni'):
    """ 
    Reads all csv files about regions data and concatenates them in a 
    data frame.
    """
    
    all_files_paths = os.path.join(path, "*.csv")
    all_files = glob.glob(all_files_paths)
    return pd.concat((pd.read_csv(file) for file in all_files))



def extract_single_region_data(df, region):
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

        
    return region_df


def compute_ti_oppupation_per_regions(df, save_image=False):
    """
    Computes and plots relations between occupied TI places and available ones,
    for some regions of interest. 

    """
    marche = extract_single_region_data(df, "Marche")
    lombardia = extract_single_region_data(df, "Lombardia")
    campania = extract_single_region_data(df, "Campania")
    molise = extract_single_region_data(df, "Molise")
    
    
    # Plot the data
    plt.plot(molise['data'], molise['occupazione_ti'], label='Molise', c='#4CD233')
    plt.plot(lombardia['data'], lombardia['occupazione_ti'], label='Lombardia', c='#FF4333')
    plt.plot(campania['data'], campania['occupazione_ti'], label='Campania', c='#F8B510')
    plt.plot(marche['data'], marche['occupazione_ti'], label='Marche', c='#3391FF')

    
    
    plt.axhline(y=0.4, color='r', linestyle='-')
    plt.axhline(y=1, color='r', linestyle='-')
    
    
    plt.gcf().autofmt_xdate()
    
    plt.grid(True)
    
    plt.title('Posti TI occupati/disponibili per regioni')
    plt.xlabel('Date')
    plt.ylabel('Posti TI occupati/disponibili')
    plt.legend()
    
    if save_image:
        plt.savefig('ti_per_regioni.png', dpi=300)
    
    plt.show()
    
    

def compute_rec_with_symptoms(df, save_image=False):
    """
    Computes and plots recovered with symptoms. 

    """
    marche = extract_single_region_data(df, "Marche")
    lombardia = extract_single_region_data(df, "Lombardia")
    campania = extract_single_region_data(df, "Campania")
    molise = extract_single_region_data(df, "Molise")
    
    
    # Plot the data
    plt.plot(molise['data'], molise['ricoverati_con_sintomi'], label='Molise', c='#4CD233')
    plt.plot(lombardia['data'], lombardia['ricoverati_con_sintomi'], label='Lombardia', c='#FF4333')
    plt.plot(campania['data'], campania['ricoverati_con_sintomi'], label='Campania', c='#F8B510')
    plt.plot(marche['data'], marche['ricoverati_con_sintomi'], label='Marche', c='#3391FF')
    
    plt.gcf().autofmt_xdate()
    
    plt.grid(True)
    
    plt.title('Ricoverati con sintomi')
    plt.xlabel('Date')
    plt.ylabel('Ricoverati con sintomi')
    plt.legend()
    
    if save_image:
        plt.savefig('ricoverati_con_sintomi.png', dpi=300)
    
    plt.show()
    
    
    
def compute_daily_cases(df, save_image=False):
    """
    Computes and plots relations between occupied TI places and available ones,
    for some regions of interest. 

    """
    marche = extract_single_region_data(df, "Marche")
    lombardia = extract_single_region_data(df, "Lombardia")
    campania = extract_single_region_data(df, "Campania")
    molise = extract_single_region_data(df, "Molise")
    
    
    # Plot the data
    plt.plot(molise['data'], molise['nuovi_positivi'], label='Molise', c='#4CD233')
    plt.plot(lombardia['data'], lombardia['nuovi_positivi'], label='Lombardia', c='#FF4333')
    plt.plot(campania['data'], campania['nuovi_positivi'], label='Campania', c='#F8B510')
    plt.plot(marche['data'], marche['nuovi_positivi'], label='Marche', c='#3391FF')
    
    
    plt.gcf().autofmt_xdate()
    
    plt.grid(True)
    
    plt.title('Nuovi positivi giornalieri per regione')
    plt.xlabel('Date')
    plt.ylabel('Nuovi positivi')
    plt.legend()
    
    if save_image:
        plt.savefig('positivi_per_regioni.png', dpi=300)
    
    plt.show()
  