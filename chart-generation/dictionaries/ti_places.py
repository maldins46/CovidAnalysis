#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intensive therapy available places, as a dictionary. Manually added from:
https://www.infodata.ilsole24ore.com/2020/10/15/terapie-intensive-scopri-in-tempo-reale-quanti-posti-sono-occupati/
Source: Quotidiano Sanità, Report Commissario Arcuri, areasional data
@author: riccardomaldini
"""

from . import area_codes as areas

ti_places_dict = {
    areas.italia: 6458,
    areas.abruzzo: 148,
    areas.basilicata: 73,
    areas.calabria: 239,
    areas.campania: 505,
    areas.emilia_romagna: 634,
    areas.friuli: 1080,
    areas.lazio: 847,
    areas.liguria: 209,
    areas.lombardia: 1036,
    areas.marche: 143,
    areas.molise: 34,
    areas.bolzano: 55,
    areas.trento: 51,
    areas.piemonte: 575,
    areas.puglia: 369,
    areas.sardegna: 9,
    areas.sicilia: 588,
    areas.toscana: 523,
    areas.umbria: 117,
    areas.valle_daosta: 20,
    areas.veneto: 1016
}
