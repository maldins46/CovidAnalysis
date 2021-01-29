#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intensive therapy available places, as a dictionary. Manually added from:
https://www.infodata.ilsole24ore.com/2020/10/15/terapie-intensive-scopri-in-tempo-reale-quanti-posti-sono-occupati/
Source: Quotidiano Sanità, Report Commissario Arcuri, areasional data
@author: riccardomaldini
"""

from . import area_codes as areas

area_names_dict = {
    areas.italia: "Italia",
    areas.abruzzo: "Abruzzo",
    areas.basilicata: "Basilicata",
    areas.calabria: "Calabria",
    areas.campania: "Campania",
    areas.emilia_romagna: "Emilia-Romagna",
    areas.friuli: "Friuli Venezia Giulia",
    areas.lazio: "Lazio",
    areas.liguria: "Liguria",
    areas.lombardia: "Lombardia",
    areas.marche: "Marche",
    areas.molise: "Molise",
    areas.bolzano: "P.A. Bolzano",
    areas.trento: "P.A. Trento",
    areas.piemonte: "Piemonte",
    areas.puglia: "Puglia",
    areas.sardegna: "Sardegna",
    areas.sicilia: "Sicilia",
    areas.toscana: "Toscana",
    areas.umbria: "Umbria",
    areas.valle_daosta: "Valle d'Aosta",
    areas.veneto: "Veneto",
    areas.ancona: "Ancona",
    areas.macerata: "Macerata",
    areas.fermo: "Fermo",
    areas.ascoli_piceno: "Ascoli Piceno",
    areas.pesaro_urbino: "Pesaro e Urbino"
}
