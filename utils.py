#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General mathematical and analytical utilities, used in various parts of the module.
@author: riccardomaldini
"""

import numpy as np
import math
import matplotlib.pyplot as plt


def compute_x_days_mov_average(array, window=7):
    """
    Computes an x-days-moving-average on the given array, of the given
    dataframe, and returns the computed column, padded in the center.
    """

    column_ma = np.convolve(array, np.ones(window)/window, mode='valid')
    left_padding = np.full(math.ceil((window-1)/2), float('NaN'))
    right_padding = np.full(math.floor((window-1)/2), float('NaN'))

    return np.concatenate((left_padding, column_ma, right_padding))


def compute_rt(new_positives_array_raw):
    """
    Computes the rt index, with SIR method (simplified version of EpiEstim)
    https://www.scienzainrete.it/articolo/modo-semplice-calcolare-rt/roberto-battiston/2020-11-20
    """

    # Inverse healing time in days (avg)
    gamma = 1/9 - 1

    # compute the 7-days moving average for new positives, for a stable I(t)
    new_positives_ma = compute_x_days_mov_average(new_positives_array_raw, 7)

    # compute ln(I(t))
    column_log = np.log(new_positives_ma)

    # compute(d ln(I(t)) dt)
    column_log_diff = np.diff(column_log)

    # add a NaN value before the array, as diff returns an array of dimension n-1
    column_rt_padded = np.insert(column_log_diff, 0, float('NaN'))

    # compute rt with SIR
    column_rt = (column_rt_padded + gamma) / gamma

    # stabilize value
    stable_rt = compute_x_days_mov_average(column_rt, 7)

    return stable_rt


def scale_per_x_inhabitants(array, population, per_inhabitants=100000):
    return array / population * per_inhabitants