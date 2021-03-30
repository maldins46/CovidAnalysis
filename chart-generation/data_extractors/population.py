#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor for population data.
@author: riccardomaldini
"""

import csv


def extract_population_dict(path='./data/population.csv'):
    """
    Extracts a dictionary that keeps track of the population for each administrative area.
    The index column is 'istat_code', the population column is 'population'.
    :rtype: Dictionary
    """

    with open(path, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        population_dict = {rows[0]: int(rows[1]) for rows in reader}

    return population_dict


# Pre-computed data. Use this to avoid re-generating the data structure each time
population_dict = extract_population_dict()
