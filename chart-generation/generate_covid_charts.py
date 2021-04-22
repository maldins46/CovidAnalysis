#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates all charts linked to the covid evolution in italy.
@author: riccardomaldini
"""

from charts import italy as chrt_italy
from charts import marche as chrt_marche
from geocharts import italy as geoc_italy
from geocharts import marche as geoc_marche
from summaries import italy as summ_italy, marche as summ_marche
from pathlib import Path

# Generate folder if not present
Path("./charts/covid").mkdir(parents=True, exist_ok=True)

chrt_italy.parameters(save_image=True)
chrt_italy.weekly_incidence(save_image=True)
chrt_italy.rt_per_regions(save_image=True)
chrt_italy.ti_occupation(save_image=True)

chrt_marche.parameters(save_image=True)
chrt_marche.weekly_incidence(save_image=True)
chrt_marche.cases_per_provinces_abs(save_image=True)

geoc_italy.ti_occupation(save_image=True)
geoc_italy.weekly_incidence_regions(save_image=True)
geoc_italy.weekly_incidence_provinces(save_image=True)
geoc_italy.weekly_increment_regions(save_image=True)
geoc_italy.weekly_increment_provinces(save_image=True)
geoc_italy.weekly_increment_ti(save_image=True)

geoc_marche.new_positives(save_image=True)
geoc_marche.weekly_incidence(save_image=True)
geoc_marche.weekly_increment(save_image=True)

summ_italy.compute_summary(save=True)
summ_marche.compute_summary(save=True)
