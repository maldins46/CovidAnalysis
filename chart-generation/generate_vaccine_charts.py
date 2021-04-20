#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates all charts linked to the vaccines situation in italy.
@author: riccardomaldini
"""

from charts import vaccines as chrt_vac
from geocharts import vaccines as geoc_vac
from summaries import vaccines as summ_vac
from pathlib import Path

# Generate folder if not present
Path("./charts/vaccines").mkdir(parents=True, exist_ok=True)

chrt_vac.immunes_percentage(save_image=True)
chrt_vac.regional_doses(save_image=True)
chrt_vac.adm_doses_marche(save_image=True)
chrt_vac.adm_doses_italy(save_image=True)

geoc_vac.adm_doses(save_image=True)
geoc_vac.immunes_percentage(save_image=True)
geoc_vac.coverage_percentage(save_image=True)

summ_vac.compute_summary(save=True)
