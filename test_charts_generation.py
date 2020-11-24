#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests the correct execution of the chart generation, and the output, that should correspond
to the right portion of the dataframe.
@author: riccardomaldini
"""
import regions.analysis as regions_analysis
import provinces.analysis as provinces_analysis


def test_regions_chart_generation():
    regions_analysis.compute_ti_occupation_per_regions()
    regions_analysis.compute_daily_cases()
    regions_analysis.compute_rec_with_symptoms()
    regions_analysis.compute_death()


def test_provinces_chart_generation():
    provinces_analysis.compute_total_cases_per_provinces()
