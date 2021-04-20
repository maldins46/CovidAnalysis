#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uses the library to generate all available charts in the ./assets/ directory.
@author: riccardomaldini
"""


def test_italy_charts():
    from charts import italy
    italy.parameters()
    italy.weekly_incidence()
    italy.rt_per_regions()
    italy.ti_occupation()


def test_marche_charts():
    from charts import marche
    marche.parameters()
    marche.weekly_incidence()
    marche.cases_per_provinces_abs()


def test_vaccines_charts():
    from charts import vaccines
    vaccines.immunes_percentage()
    vaccines.regional_doses()
    vaccines.adm_doses_marche()
    vaccines.adm_doses_italy()


def test_italy_geocharts():
    from geocharts import italy
    italy.ti_occupation()
    italy.weekly_incidence_regions()
    italy.weekly_incidence_provinces()
    italy.weekly_increment_regions()
    italy.weekly_increment_provinces()


def test_vaccines_geocharts():
    from geocharts import vaccines
    vaccines.adm_doses()
    vaccines.immunes_percentage()
    vaccines.coverage_percentage()


def test_marche_geocharts():
    from geocharts import marche
    marche.new_positives()
    marche.weekly_incidence()


def test_summaries():
    from summaries import italy as sum_italy, vaccines as sum_vaccines, marche as sum_marche
    sum_italy.compute_summary()
    sum_vaccines.compute_summary()
    sum_marche.compute_summary()
