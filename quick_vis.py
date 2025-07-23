""""

    Simply quick visualization of any of the MSC grid files using xarray and matplotlib
    2D ove view

    Liam.Buchart@nrcan-rncan.gc.ca
    July 17, 2025

"""

import xarray as xr
import cfgrib
import matplotlib.pyplot as plt
import os

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
data_file = f"\\{year}{month}{day}T{model_run}Z_MSC_{data_dir}_{vis_var}_RLatLon0.09_PT{fcst_hr}H.grib2"
p = Path(data_dir).resolve()
sp = Path(save_dir).resolve()
print(str(sp))
full_data = str(p) + data_file

if os.path.exists(full_data):
    ds = xr.open_dataset(full_data, engine="cfgrib")

    lats = ds.latitude.values
    lons = ds.longitude.values

    fig = plt.figure(figsize=(12,12))
    if vis_var == "RelativeHumidity_AGL-2m":
        rh2 = ds['r2']

        print(rh2.attrs)
        rh2.plot()
        plt.savefig(str(sp) + f"{vis_var}_easyplot.png")


print("Done m'lord")