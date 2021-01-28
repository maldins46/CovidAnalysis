#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests the correct execution of the chart generation, and the output, that should correspond
to the right portion of the dataframe.
@author: riccardomaldini
"""
import regions.analysis as regions_analysis
import provinces.analysis as provinces_analysis
import national.analysis as national_analysis
import vaccines.analysis as vacc_nat
import vaccines.areas as areas


def test_national_chart_generation():
    national_analysis.compute_national_parameters()


def test_regions_chart_generation():
    regions_analysis.compute_ti_occupation_per_regions()
    regions_analysis.compute_rt_per_regions()
    regions_analysis.compute_positivity_per_regions()
    regions_analysis.compute_weekly_incidence()
    regions_analysis.compute_daily_cases()
    regions_analysis.compute_rec_with_symptoms()
    regions_analysis.compute_death()
    regions_analysis.compute_region_parameters()


def test_provinces_chart_generation():
    provinces_analysis.compute_total_cases_per_provinces()
    provinces_analysis.compute_total_cases_per_provinces_abs()


def test_vaccines_chart_generation():
    vacc_nat.compute_regional_doses()
    vacc_nat.compute_adm()
    vacc_nat.compute_adm(area_code=areas.marche)
    vacc_nat.compute_immunes_per_regions()
