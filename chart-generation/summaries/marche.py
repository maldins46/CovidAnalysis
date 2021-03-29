#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computes the JSON summary sheet.
@author: riccardomaldini
"""

from data_extractors.covid_regions import marche_df
from data_extractors.covid_provinces import marche_dict
import json
from datetime import datetime
from data_extractors.area_names import area_names_dict


def compute_summary(print_terminal=False, save=False):
    """
    Computes benchmark summary.
    """

    # TI
    ti_percentage = marche_df['occupazione_ti'].iloc[-1]

    # increment TI
    ti_rolling_7_mean = marche_df['occupazione_ti'].rolling(7).mean()
    ti_perc_increment = (ti_rolling_7_mean.iloc[-1] - ti_rolling_7_mean.iloc[-2])\
        / ti_rolling_7_mean.iloc[-2]

    # new positives
    new_positives = marche_df['nuovi_positivi'].iloc[-1]

    # increment new positives
    positives_rolling_7_mean = marche_df['nuovi_positivi'].rolling(7).mean()
    positives_perc_increment = (positives_rolling_7_mean.iloc[-1] - positives_rolling_7_mean.iloc[-2])\
        / positives_rolling_7_mean.iloc[-2]

    # weekly positives
    positives_rolling_7_sum = marche_df['nuovi_positivi'].rolling(7).sum()
    weekly_new_positives = positives_rolling_7_sum.iloc[-1]

    # weekly increment
    weekly_new_positives_increment = (positives_rolling_7_sum.iloc[-1] - positives_rolling_7_sum.iloc[-8])\
        / positives_rolling_7_sum.iloc[-8]

    output_dict = {}
    output_dict.update({"lastUpdate": datetime.now().isoformat()})

    region_dict = {
            "tiPercentage": f"{ti_percentage:.4f}",
            "tiIncrement": f"{ti_perc_increment:.4f}",
            "newPositives": f"{new_positives:.0f}",
            "newPositivesIncrement": f"{positives_perc_increment:.4f}",
            "weeklyPositives": f"{weekly_new_positives:.0f}",
            "weeklyPositivesIncrement": f"{weekly_new_positives_increment:.4f}"
    }
    output_dict.update({"marche": region_dict})


    for province_code, province_data in marche_dict.items():
        # new positives
        new_positives = province_data['nuovi_positivi'].iloc[-1]

        # increment new positives
        positives_rolling_7_mean = province_data['nuovi_positivi'].rolling(7).mean()
        positives_perc_increment = (positives_rolling_7_mean.iloc[-1] - positives_rolling_7_mean.iloc[-2])\
            / positives_rolling_7_mean.iloc[-2]

        # weekly positives
        positives_rolling_7_sum = province_data['nuovi_positivi'].rolling(7).sum()
        weekly_new_positives = positives_rolling_7_sum.iloc[-1]

        # weekly increment
        weekly_new_positives_increment = (positives_rolling_7_sum.iloc[-1] - positives_rolling_7_sum.iloc[-8])\
            / positives_rolling_7_sum.iloc[-8]

        province_name_clean = area_names_dict[province_code].lower().replace(' ', '')
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
