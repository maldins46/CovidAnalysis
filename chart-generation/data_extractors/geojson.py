#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor for regional and provincial GeoDataframes, given into the required format
for the generation of Geopandas maps.
@author: riccardomaldini
"""

import geopandas as gpd
import pandas as pd

# Constants
RAW_REG_ITALY = gpd.read_file('https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson')
RAW_PROV_ITALY = gpd.read_file('https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_provinces.geojson')


def extract_regions_geodf():
    """
    Creates a GeoDataframe including italian regions, indexed by ISTAT code, including Trento and Bolzano provinces
    instead of Trentino Alto Adige.
    :rtype: GeoDataframe
    """

    reg_italy = RAW_REG_ITALY
    prov_italy = RAW_PROV_ITALY

    # regions + trento & bolzano
    reg_italy = pd.concat([reg_italy, prov_italy[prov_italy['prov_istat_code_num'] == 21],
                          prov_italy[prov_italy['prov_istat_code_num'] == 22]],
                          ignore_index=True)

    reg_italy['reg_istat_code'] = reg_italy.apply(lambda x: '21' if x['prov_istat_code_num'] == 21 else x['reg_istat_code'],
                                                  axis=1)
    reg_italy['reg_istat_code'] = reg_italy.apply(lambda x: '22' if x['prov_istat_code_num'] == 22 else x['reg_istat_code'],
                                                  axis=1)

    reg_italy['codice_regione'] = reg_italy['reg_istat_code']
    reg_italy = reg_italy[reg_italy['codice_regione'] != '04']

    return reg_italy


def extract_provinces_geodf():
    """
    Creates a GeoDataframe including italian provinces, indexed by ISTAT code.
    :rtype: GeoDataframe
    """

    prov_italy = RAW_PROV_ITALY

    # Format as text
    prov_italy['codice_provincia'] = prov_italy['prov_istat_code']

    return prov_italy


# Pre-computed data. Use this to avoid re-generating the data structure each time
regions_geodf = extract_regions_geodf()
provinces_geodf = extract_provinces_geodf()
