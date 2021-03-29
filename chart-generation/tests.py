#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uses the library to generate all available charts in the ./assets/ directory.
@author: riccardomaldini
"""
#%%
#from charts import italy

#italy.parameters(show=True)
#italy.weekly_incidence(show=True)
#italy.rt_per_regions(show=True)
#italy.ti_occupation(show=True)

#from charts import marche
#marche.parameters(show=True)
#marche.weekly_incidence(show=True)
#marche.cases_per_provinces_abs(show=True)

from geocharts import italy
italy.ti_occupation(show=True)
italy.weekly_incidence_regions(show=True)
italy.weekly_incidence_provinces(show=True)