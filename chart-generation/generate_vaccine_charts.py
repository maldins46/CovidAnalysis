#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates all charts linked to the vaccines situation in italy.
@author: riccardomaldini
"""

from charts import vaccines
vaccines.immunes_percentage(save_image=True)
vaccines.regional_doses(save_image=True)
vaccines.adm_doses_marche(save_image=True)
vaccines.adm_doses_italy(save_image=True)

from geocharts import vaccines
vaccines.adm_doses(save_image=True)
vaccines.immunes_percentage(save_image=True)

from summaries import vaccines as sum_vaccines
sum_vaccines.compute_summary(save=True)
