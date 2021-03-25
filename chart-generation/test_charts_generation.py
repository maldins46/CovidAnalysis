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
import dictionaries.area_codes as areas
import national.summary as national_summary
import regions.summary as benchmark_summary
import provinces.summary as marche_summary
import vaccines.summary as vaccines_summary
import regions.geoanalysis as geo_reg
import vaccines.geoanalysis as geo_vac
import provinces.geoanalysis as geo_prov


def test_geo_generation():
    geo_reg.compute_incidence_map(save_image=False, show=False)
    geo_reg.compute_ti_map(save_image=False, show=False)
    geo_vac.compute_adm_doses_map(save_image=False, show=False)
    geo_vac.compute_immunes_percentage_map(save_image=False, show=False)
    geo_prov.compute_incidence_prov_map(save_image=False, show=False)
    geo_prov.compute_incidence_marche_map(save_image=False, show=False)


def test_summary_generation():
    national_summary.compute_summary(save=False, print_terminal=False)
    benchmark_summary.compute_summary(save=False, print_terminal=False)
    marche_summary.compute_marche_summary(print_terminal=True, save=False)
    vaccines_summary.compute_summary(save=True, print_terminal=False)


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
    regions_analysis.compute_region_parameters(region_code=areas.marche)


def test_provinces_chart_generation():
    provinces_analysis.compute_total_cases_per_provinces()
    provinces_analysis.compute_total_cases_per_provinces_abs()
    provinces_analysis.compute_weekly_incidence()


def test_vaccines_chart_generation():
    vacc_nat.compute_regional_doses()
    vacc_nat.compute_adm()
    vacc_nat.compute_adm(area_code=areas.marche)
    vacc_nat.compute_immunes_per_regions()
