"""

    Generate 30 year mean, median, std, 25th, 75th, 
    10th, and 90th percentiles of wind speed, direction, 
    and wind run for each month and meteorological 
    season (DJF, MAM, JJA, SON).

    Input: nil
    Ouput: 1990-2020 monthly and seasonal mean files (in .h5 files)
           of wind speed, direction, and run.

    Liam.Buchart@nrcan-rncan.gc.ca
    September 12, 2025

"""
#%%
import os
import json

import xarray as xr

data_dir = "./climatology/"

months = range(1, 12+1)
seasons = {
    "DJF": [12, 1, 2],
    "MAM": [3, 4, 5],
    "JJA": [6, 7, 8],
    "SON": [9, 10, 11]
}