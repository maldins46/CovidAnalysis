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


def distanced_diff(array, distance=7):
    """
    Computes for each element of the given array the difference between the n-th element with
    the n-th - distance element.
    """

    if type(array) is np.ndarray:
        np_array = array
    else:
        np_array = array.to_numpy()

    distanced_diff = np_array[distance:] - np_array[:-distance]
    left_padding = np.full(distance, float('NaN'))
    return np.concatenate((left_padding, distanced_diff))


def compute_rt(tot_cases, tot_healed, tot_death):
    """
    Computes and plots RT for some regions of interest, with SIRD model applied as by INFN, with some modifications for
    handling the shift between new positives and deaths-healings.
    https://covid19.infn.it/banner/Approfondimenti.pdf
    """

    delta_tot_positives = distanced_diff(tot_cases.to_numpy(), 7)
    delta_tot_healed = distanced_diff(tot_healed.to_numpy(), 7)
    delta_tot_death = distanced_diff(tot_death.to_numpy(), 7)

    sh_delta_tot_positives = delta_tot_positives[:-7]
    sh_delta_tot_healed = delta_tot_healed[7:]
    sh_delta_tot_death = delta_tot_death[7:]

    column_rt = sh_delta_tot_positives / (sh_delta_tot_healed + sh_delta_tot_death)

    # add a NaN value before the array, as diff returns an array of dimension n-7
    right_padding = np.full(7, float('NaN'))
    rt_padded = np.concatenate((column_rt, right_padding))

    return compute_x_days_mov_average(rt_padded, 4)


def scale_per_x_inhabitants(array, population, per_inhabitants=100000):
    return array / population * per_inhabitants
