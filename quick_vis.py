""""

    Simply quick visualization of any of the MSC grid files using xarray and matplotlib
    2D ove view

    Liam.Buchart@nrcan-rncan.gc.ca
    July 17, 2025

"""

import xarray as xr
import cfgrib
import matplotlib.pyplot as plt

from pathlib import Path

##### USER DEFINED VARIABLES #####
data_dir = "RDPS"
save_dir = "/FIGURES/"
# consult the variable list or any data directory (RDPS, HRDPS, etc.) for names/conventions
vis_var = "RelativeHumidity_AGL-2m"
year = "2025"
month = "07"
day = "02"
model_run = "12"
fcst_hr = "008"
##### END USER DEFINED VARIABLES #####

# define the path to the data
data_path = str(Path.cwd()) + "/" + data_dir + "/" + year + month + day + "/" + model_run + "/"
data_file = f"{year}{month}{day}_T{model_run}_MSC_{data_dir}_{vis_var}_RLatLon0.09_PT{fcst_hr}H.grib2"
print(data_path + "    "  + data_file)

ds = xr.load_dataset(data_path + data_file, engine="cfgrib")

print(ds)