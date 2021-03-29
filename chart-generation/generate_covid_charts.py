#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates all charts linked to the covid evolution in italy.
@author: riccardomaldini
"""

from charts import italy
italy.parameters(save_image=True)
italy.weekly_incidence(save_image=True)
italy.rt_per_regions(save_image=True)
italy.ti_occupation(save_image=True)

from charts import marche
marche.parameters(save_image=True)
marche.weekly_incidence(save_image=True)
marche.cases_per_provinces_abs(save_image=True)

from geocharts import italy
italy.ti_occupation(show=True)
italy.weekly_incidence_regions(show=True)
italy.weekly_incidence_provinces(show=True)

from geocharts import marche
marche.new_positives()
marche.weekly_incidence()

from summaries import italy as sum_italy, marche as sum_marche
sum_italy.compute_summary(save=True)
sum_marche.compute_summary(save=True)