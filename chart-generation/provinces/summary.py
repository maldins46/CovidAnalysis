#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computes the JSON summary sheet.
@author: riccardomaldini
"""

from .data_extractor import provinces_of_marche_data
import json
from datetime import datetime
from dictionaries.area_names import area_names_dict as area_names


def compute_marche_summary(print_terminal=True, save=False):
    """
    Computes provinces summary.
    """

    output_dict = {}
    output_dict.update({"lastUpdate": datetime.now().isoformat()})

    for province_code, province_data in provinces_of_marche_data.items():
        # new positives
        new_positives = province_data['incremento_casi'].iloc[-1]

        # increment new positives
        positives_rolling_7_mean = province_data['incremento_casi'].rolling(7).mean()
        positives_perc_increment = (positives_rolling_7_mean.iloc[-1] - positives_rolling_7_mean.iloc[-2])\
            / positives_rolling_7_mean.iloc[-2]

        # weekly positives
        positives_rolling_7_sum = province_data['incremento_casi'].rolling(7).sum()
        weekly_new_positives = positives_rolling_7_sum.iloc[-1]

        # weekly increment
        weekly_new_positives_increment = (positives_rolling_7_sum.iloc[-1] - positives_rolling_7_sum.iloc[-8])\
            / positives_rolling_7_sum.iloc[-8]

        province_name_clean = area_names[province_code].lower().replace(' ', '')
        province_dict = {
            "newPositives": f"{new_positives:.0f}",
            "newPositivesIncrement": f"{positives_perc_increment:.4f}",
            "weeklyPositives": f"{weekly_new_positives:.0f}",
            "weeklyPositivesIncrement": f"{weekly_new_positives_increment:.4f}"
        }
        output_dict.update({f"{province_name_clean}": province_dict})

    if save:
        with open('./assets/marche_summary.json', 'w') as f:
            json.dump(output_dict, f)

    if print_terminal:
        json_output = json.dumps(output_dict)
        print(json_output)
