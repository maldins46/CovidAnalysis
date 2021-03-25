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
    areas.abruzzo: 189,
    areas.basilicata: 88,
    areas.calabria: 152,
    areas.campania: 620,
    areas.emilia_romagna: 757,
    areas.friuli: 175,
    areas.lazio: 943,
    areas.liguria: 217,
    areas.lombardia: 1232,
    areas.marche: 216,
    areas.molise: 34,
    areas.bolzano: 77,
    areas.trento: 90,
    areas.piemonte: 628,
    areas.puglia: 458,
    areas.sardegna: 180,
    areas.sicilia: 799,
    areas.toscana: 559,
    areas.umbria: 130,
    areas.valle_daosta: 20,
    areas.veneto: 1000
}
