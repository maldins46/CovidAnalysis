#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example execution of the scripts.
@author: riccardomaldini
"""
import regions_analysis
import provinces_analysis

regions_analysis.compute_ti_occupation_per_regions(save_image=True, show=False)
regions_analysis.compute_daily_cases(save_image=True, show=False)
regions_analysis.compute_rec_with_symptoms(save_image=True, show=False)
regions_analysis.compute_death(save_image=True, show=False)
provinces_analysis.compute_total_cases_per_provinces(save_image=True, show=False)
