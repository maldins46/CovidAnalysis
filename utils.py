#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General mathematical and analytical utilities, used in various parts of the module.
@author: riccardomaldini
"""

import numpy as np
import math


def compute_x_days_mov_average(array, window=7):
    """
    Computes an x-days-moving-average on the given array, of the given
    dataframe, and returns the computed column, padded in the center.
    """

    column_ma = np.convolve(array, np.ones(window)/window, mode='valid')
    left_padding = np.full(math.ceil((window-1)/2), float('NaN'))
    right_padding = np.full(math.floor((window-1)/2), float('NaN'))

    return np.concatenate((left_padding, column_ma, right_padding))


def compute_rt(tot_cases, tot_healed, tot_death):
    """
    Computes and plots RT for some regions of interest, with SIRD model applied as by INFN, with some modifications for
    handling the shift between new positives and deaths-healings.
    https://covid19.infn.it/banner/Approfondimenti.pdf    
    """
    distanced_diff = lambda array, distance : array[distance:] - array[:-distance]


    delta_tot_positives = distanced_diff(np.log(tot_cases.to_numpy()), 7)
    delta_tot_healed = distanced_diff(np.log(tot_healed.to_numpy()), 7)
    delta_tot_death = distanced_diff(np.log(tot_death.to_numpy()), 7)

    sh_delta_tot_positives = delta_tot_positives[:-8]
    sh_delta_tot_healed = delta_tot_healed[8:]
    sh_delta_tot_death = delta_tot_death[8:]

    column_rt = sh_delta_tot_positives / (sh_delta_tot_healed + sh_delta_tot_death)

    # add a NaN value before the array, as diff returns an array of dimension n-7
    left_padding = np.full(7, float('NaN'))
    right_padding = np.full(8, float('NaN'))

    column_rt_padded = np.concatenate((left_padding, column_rt, right_padding))

    stable_rt = compute_x_days_mov_average(column_rt_padded, 14)

    return stable_rt


def scale_per_x_inhabitants(array, population, per_inhabitants=100000):
    return array / population * per_inhabitants
