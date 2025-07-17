""""

    Simply quick visualization of any of the MSC grid files using xarray and matplotlib
    2D ove view

    Liam.Buchart@nrcan-rncan.gc.ca
    July 17, 2025

"""

import xarray as xr
import matplotlib.pyplot as plt

from pathlib import Path

##### USER DEFINED VARIABLES #####
data_dir = "RDPS"
# consult the variable list or any data directory (RDPS, HRDPS, etc.) for names/conventions
vis_var = "RelativeHumidity"
year = "2025"
month = "07"
day = "02"
model_run = "12"
fcst_hr = "008"
##### END USER DEFINED VARIABLES #####

