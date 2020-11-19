#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example execution of the scripts.
@author: riccardomaldini
"""
import covid_analysis as covid
  
# Create dataframe, extract some region data, plot all available info
df = covid.extract_regions_data()
covid.compute_ti_occupation_per_regions(df, save_image=True, show=False)
covid.compute_daily_cases(df, save_image=True, show=False)
covid.compute_rec_with_symptoms(df, save_image=True, show=False)