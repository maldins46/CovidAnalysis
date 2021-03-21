#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computes the JSON summary sheet.
@author: riccardomaldini
"""

from .data_extractor import benchmark_regions_data
import json
from datetime import datetime
from dictionaries.area_names import area_names_dict as area_names


def compute_summary(print_terminal=True, save=False):
    """
    Computes benchmark summary.
    """

    output_dict = {}
    output_dict.update({"lastUpdate": datetime.now().isoformat()})

    for region_code, region_data in benchmark_regions_data.items():
        # TI
        ti_percentage = region_data['occupazione_ti'].iloc[-1]

        # increment TI
        ti_rolling_7_mean = region_data['occupazione_ti'].rolling(7).mean()
        ti_perc_increment = (ti_rolling_7_mean.iloc[-1] - ti_rolling_7_mean.iloc[-2])\
            / ti_rolling_7_mean.iloc[-2]

        # new positives
        new_positives = region_data['nuovi_positivi'].iloc[-1]

        # increment new positives
        positives_rolling_7_mean = region_data['nuovi_positivi'].rolling(7).mean()
        positives_perc_increment = (positives_rolling_7_mean.iloc[-1] - positives_rolling_7_mean.iloc[-2])\
            / positives_rolling_7_mean.iloc[-2]

        # weekly positives
        positives_rolling_7_sum = region_data['nuovi_positivi'].rolling(7).sum()
        weekly_new_positives = positives_rolling_7_sum.iloc[-1]

        # weekly increment
        weekly_new_positives_increment = (positives_rolling_7_sum.iloc[-1] - positives_rolling_7_sum.iloc[-8])\
            / positives_rolling_7_sum.iloc[-8]

        region_name_clean = area_names[region_code].lower().replace(' ', '_')
        region_dict = {
            "tiPercentage": f"{ti_percentage:.4f}",
            "tiIncrement": f"{ti_perc_increment:.4f}",
            "newPositives": f"{new_positives:.0f}",
            "newPositivesIncrement": f"{positives_perc_increment:.4f}",
            "weeklyPositives": f"{weekly_new_positives:.0f}",
            "weeklyPositivesIncrement": f"{weekly_new_positives_increment:.4f}"
        }
        output_dict.update({f"{region_name_clean}": region_dict})

    if save:
        with open('./assets/benchmark_summary.json', 'w') as f:
            json.dump(output_dict, f)

    if print_terminal:
        json_output = json.dumps(output_dict)
        print(json_output)
