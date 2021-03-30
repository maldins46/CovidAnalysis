#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computes the JSON summary sheet.
@author: riccardomaldini
"""

import json
from datetime import datetime
from data_extractors.area_names import area_names_dict
from data_extractors.vaccines_regions import benchmark_dict
from data_extractors.vaccines_italy import italy_df


def compute_summary(print_terminal=False, save=False):
    """
    Computes benchmark summary.
    """

    output_dict = {}
    output_dict.update({"lastUpdate": datetime.now().isoformat()})

    # perc. popolazione immunizzata
    full_vacc_population = italy_df['seconda_dose_totale_storico_su_pop'].iloc[-1]

    # tot. dosi di oggi e incremento
    tot_shots = italy_df['totale'].iloc[-1]
    tot_shots_rolling_7_mean = italy_df['totale'].rolling(7).mean()
    tot_shots_increment = (tot_shots_rolling_7_mean.iloc[-1] - tot_shots_rolling_7_mean.iloc[-2])\
        / tot_shots_rolling_7_mean.iloc[-2]

    # prime dosi e incremento
    first_shot = italy_df['prima_dose'].iloc[-1]
    first_shot_rolling_7_mean = italy_df['prima_dose'].rolling(7).mean()
    first_shot_increment = (first_shot_rolling_7_mean.iloc[-1] - first_shot_rolling_7_mean.iloc[-2])\
        / first_shot_rolling_7_mean.iloc[-2]

    # seconde dosi e incremento
    second_shot = italy_df['seconda_dose'].iloc[-1]
    second_shot_rolling_7_mean = italy_df['seconda_dose'].rolling(7).mean()
    second_shot_increment = (second_shot_rolling_7_mean.iloc[-1] - second_shot_rolling_7_mean.iloc[-2])\
        / second_shot_rolling_7_mean.iloc[-2]

    italy_dict = {
        "fullVaccPopulation": f"{full_vacc_population:.4f}",
        "dailyShots": f"{tot_shots:.0f}",
        "dailyShotsIncrement": f"{tot_shots_increment:.4f}",
        "dailyFirstShots": f"{first_shot:.0f}",
        "dailyFirstShotsIncrement": f"{first_shot_increment:.4f}",
        "dailySecondShots": f"{second_shot:.0f}",
        "dailySecondShotsIncrement": f"{second_shot_increment:.4f}"
    }
    output_dict.update({"italy": italy_dict})

    for region_code, region_data in benchmark_dict.items():
        # perc. popolazione immunizzata
        full_vacc_population = region_data['seconda_dose_totale_storico_su_pop'].iloc[-1]

        # tot. dosi di oggi e incremento
        tot_shots = region_data['totale'].iloc[-1]
        tot_shots_rolling_7_mean = region_data['totale'].rolling(7).mean()
        tot_shots_increment = (tot_shots_rolling_7_mean.iloc[-1] - tot_shots_rolling_7_mean.iloc[-2])\
            / tot_shots_rolling_7_mean.iloc[-2]

        # prime dosi e incremento
        first_shot = region_data['prima_dose'].iloc[-1]
        first_shot_rolling_7_mean = region_data['prima_dose'].rolling(7).mean()
        first_shot_increment = (first_shot_rolling_7_mean.iloc[-1] - first_shot_rolling_7_mean.iloc[-2])\
            / first_shot_rolling_7_mean.iloc[-2]

        # seconde dosi e incremento
        second_shot = region_data['seconda_dose'].iloc[-1]
        second_shot_rolling_7_mean = region_data['seconda_dose'].rolling(7).mean()
        second_shot_increment = (second_shot_rolling_7_mean.iloc[-1] - second_shot_rolling_7_mean.iloc[-2])\
            / second_shot_rolling_7_mean.iloc[-2]

        region_name_clean = area_names_dict[region_code].lower().replace(' ', '_')
        region_dict = {
            "fullVaccPopulation": f"{full_vacc_population:.4f}",
            "dailyShots": f"{tot_shots:.0f}",
            "dailyShotsIncrement": f"{tot_shots_increment:.4f}",
            "dailyFirstShots": f"{first_shot:.0f}",
            "dailyFirstShotsIncrement": f"{first_shot_increment:.4f}",
            "dailySecondShots": f"{second_shot:.0f}",
            "dailySecondShotsIncrement": f"{second_shot_increment:.4f}"
        }
        output_dict.update({f"{region_name_clean}": region_dict})

    if save:
        with open('./charts/vaccines/vaccines_summary.json', 'w') as f:
            json.dump(output_dict, f)

    if print_terminal:
        json_output = json.dumps(output_dict)
        print(json_output)
