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
import vaccines.summary as vaccines_summary
import regions.geoanalysis as geo_reg
import vaccines.geoanalysis as geo_vac
import provinces.geoanalysis as geo_prov
import regions.geoanalysis as geo_reg
import vaccines.geoanalysis as geo_vac
import provinces.geoanalysis as geo_prov

geo_reg.compute_incidence_map(save_image=True, show=False)
geo_reg.compute_ti_map(save_image=True, show=False)

geo_vac.compute_adm_doses_map(save_image=True, show=False)
geo_vac.compute_immunes_percentage_map(save_image=True, show=False)

geo_prov.compute_incidence_prov_map(save_image=True, show=False)
geo_prov.compute_incidence_marche_map(save_image=True, show=False)

vaccines_summary.compute_summary(save=True, print_terminal=False)
marche_summary.compute_marche_summary(save=True, print_terminal=False)
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

provinces_analysis.compute_total_cases_per_provinces_abs(save_image=True, show=False)
provinces_analysis.compute_weekly_incidence(save_image=True, show=False)
