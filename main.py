#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example execution of the scripts.
@author: riccardomaldini
"""
import covidAnalysis as covid
  
# Create dataframe, extract some region data, plot all available info
df = covid.extract_regions_data()
covid.compute_ti_oppupation_per_regions(df, True)
covid.compute_daily_cases(df, True)
covid.compute_rec_with_symptoms(df, True)
