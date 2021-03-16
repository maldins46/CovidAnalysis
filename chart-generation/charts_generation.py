#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uses the library to generate all available charts in the ./assets/ directory.
@author: riccardomaldini
"""
import regions.analysis as regions_analysis
import provinces.analysis as provinces_analysis
import national.analysis as national_analysis
import vaccines.analysis as vacc_nat
import dictionaries.area_codes as areas
import national.summary as national_summary
import regions.summary as benchmark_summary
import provinces.summary as marche_summary

marche_summary.compute_marche_summary(print_terminal=True, save=False)
benchmark_summary.compute_summary(save=True, print_terminal=False)
national_summary.compute_summary(save=True, print_terminal=False)
vacc_nat.compute_regional_doses(save_image=True, show=False)
vacc_nat.compute_adm(save_image=True, show=False)
vacc_nat.compute_adm(save_image=True, show=False, area_code=areas.marche)
vacc_nat.compute_immunes_per_regions(save_image=True, show=False)

national_analysis.compute_national_parameters(save_image=True, show=False)

regions_analysis.compute_ti_occupation_per_regions(save_image=True, show=False)
regions_analysis.compute_rt_per_regions(save_image=True, show=False)
regions_analysis.compute_weekly_incidence(save_image=True, show=False)
regions_analysis.compute_positivity_per_regions(save_image=True, show=False)
regions_analysis.compute_daily_cases(save_image=True, show=False)
regions_analysis.compute_region_parameters(save_image=True, show=False, region_code=areas.marche)

provinces_analysis.compute_total_cases_per_provinces(save_image=True, show=False)
provinces_analysis.compute_total_cases_per_provinces_abs(save_image=True, show=False)
