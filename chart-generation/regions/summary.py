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
    output_dict["upd_date"] = datetime.now().isoformat(),

    for region_code, region_data in benchmark_regions_data.items():
        # TI
        ti_percentage = region_data['occupazione_ti'].iloc[-1]

        # increment TI
        ti_percentage_before_yest = region_data['occupazione_ti'].iloc[-2]
        ti_increment = ti_percentage - ti_percentage_before_yest
        ti_perc_increment = ti_increment / ti_percentage_before_yest

        # tot. new positives yesterday
        yesterday = region_data['nuovi_positivi'].iloc[-1]

        # perc. increment positives 1 day
        before_yesterday = region_data['nuovi_positivi'].iloc[-2]
        increment = yesterday - before_yesterday
        perc_increment = increment / before_yesterday

        # perc. increment today on latest 4 week
        one_week_ago = region_data['nuovi_positivi'].iloc[-8]
        two_week_ago = region_data['nuovi_positivi'].iloc[-15]
        three_week_ago = region_data['nuovi_positivi'].iloc[-22]
        four_week_ago = region_data['nuovi_positivi'].iloc[-29]

        last_weeks_avg = (one_week_ago + two_week_ago + three_week_ago + four_week_ago) / 4
        weekly_increment = yesterday - last_weeks_avg
        perc_weekly_increment = weekly_increment / last_weeks_avg

        region_name_clean = area_names[region_code].lower().replace(' ', '_')

        output_dict[f"{region_name_clean}_ti_percentage"] = f"{ti_percentage:.4f}",
        output_dict[f"{region_name_clean}_ti_perc_increment"] = f"{ti_perc_increment:.4f}",
        output_dict[f"{region_name_clean}_new_positives"] = f"{yesterday:.0f}",
        output_dict[f"{region_name_clean}_perc_increment_on_yesterday"] = f"{perc_increment:.4f}",
        output_dict[f"{region_name_clean}_perc_increment_on_4_weeks"] = f"{perc_weekly_increment:.4f}"

    if save:
        with open('./assets/benchmark_summary.json', 'w') as f:
            json.dump(output_dict, f)

    if print_terminal:
        json_output = json.dumps(output_dict)
        print(json_output)
