#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example execution of the scripts.
@author: riccardomaldini
"""
import covid_analysis as covid
  
covid.compute_ti_occupation_per_regions(save_image=True, show=False)
covid.compute_daily_cases(save_image=True, show=False)
covid.compute_rec_with_symptoms(save_image=True, show=False)
covid.compute_death(save_image=True, show=False)