#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor for TI places data.
@author: riccardomaldini
"""

import csv


def extract_ti_places_dict(path='/users/riccardomaldini/Desktop/CovidAnalysis/data/ti_places.csv'):
    """
    Extracts a dictionary that keeps track of the ti places for each administrative area.
    The index column is 'istat_code', the population column is 'ti'.
    :rtype: Dictionary
    """

    with open(path, mode='r',encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        population_dict = {rows[0]:int(rows[1]) for rows in reader}

    return population_dict


# Pre-computed data. Use this to avoid re-generating the data structure each time
ti_places_dict = extract_ti_places_dict()
