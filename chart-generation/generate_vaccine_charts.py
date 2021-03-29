#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates all charts linked to the vaccines situation in italy.
@author: riccardomaldini
"""

from charts import vaccines
vaccines.immunes_percentage(show=True)
vaccines.regional_doses(show=True)
vaccines.adm_doses_marche(show=True)
vaccines.adm_doses_italy(show=True)

from geocharts import vaccines
vaccines.adm_doses(show=True)
vaccines.immunes_percentage(show=True)

from summaries import vaccines as sum_vaccines
sum_vaccines.compute_summary(save=True)
