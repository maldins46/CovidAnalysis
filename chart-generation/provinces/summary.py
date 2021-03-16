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
    output_dict["upd_date"] = datetime.now().isoformat(),

    for province_code, province_data in provinces_of_marche_data.items():
        # tot. new positives yesterday
        yesterday = province_data['incremento_casi'].iloc[-1]

        # perc. increment positives 1 day
        before_yesterday = province_data['incremento_casi'].iloc[-2]
        increment = yesterday - before_yesterday
        perc_increment = increment / before_yesterday

        # perc. increment today on latest 4 week
        one_week_ago = province_data['incremento_casi'].iloc[-8]
        two_week_ago = province_data['incremento_casi'].iloc[-15]
        three_week_ago = province_data['incremento_casi'].iloc[-22]
        four_week_ago = province_data['incremento_casi'].iloc[-29]

        last_weeks_avg = (one_week_ago + two_week_ago + three_week_ago + four_week_ago) / 4
        weekly_increment = yesterday - last_weeks_avg
        perc_weekly_increment = weekly_increment / last_weeks_avg

        province_name_clean = area_names[province_code].lower().replace(' ', '_')

        output_dict[f"{province_name_clean}_new_positives"] = f"{yesterday:.0f}",
        output_dict[f"{province_name_clean}_perc_increment_on_yesterday"] = f"{perc_increment:.4f}",
        output_dict[f"{province_name_clean}_perc_increment_on_4_weeks"] = f"{perc_weekly_increment:.4f}"

    if save:
        with open('./assets/marche_summary.json', 'w') as f:
            json.dump(output_dict, f)

    if print_terminal:
        json_output = json.dumps(output_dict)
        print(json_output)
