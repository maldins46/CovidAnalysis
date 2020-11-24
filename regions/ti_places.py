#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intensive therapy available places, as a dictionary. Manually added from:
https://www.infodata.ilsole24ore.com/2020/10/15/terapie-intensive-scopri-in-tempo-reale-quanti-posti-sono-occupati/
Source: Quotidiano Sanità, Report Commissario Arcuri, regional data
@author: riccardomaldini
"""

from . import regions_names as reg

ti_places_dict = {
    reg.abruzzo: 148,
    reg.basilicata: 73,
    reg.calabria: 239,
    reg.campania: 505,
    reg.emilia_romagna: 634,
    reg.friuli: 1080,
    reg.lazio: 847,
    reg.liguria: 209,
    reg.lombardia: 1036,
    reg.marche: 143,
    reg.molise: 34,
    reg.bolzano: 55,
    reg.trento: 51,
    reg.piemonte: 575,
    reg.puglia: 369,
    reg.sardegna: 9,
    reg.sicilia: 588,
    reg.toscana: 523,
    reg.umbria: 117,
    reg.valle_daosta: 20,
    reg.veneto: 1016
}
