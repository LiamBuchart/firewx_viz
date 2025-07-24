""""

    Simply quick visualization of any of the MSC grid files using xarray and matplotlib
    2D ove view

    Liam.Buchart@nrcan-rncan.gc.ca
    July 17, 2025

"""
#%%
import numpy as np
import xarray as xr 
import matplotlib
import matplotlib.pyplot as plt
import os

from pathlib import Path

#%%
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


# %%
"""
Script to plot a 2D image of the first time slice of r2 from the data_file
"""
if os.path.exists(full_data):
    ds = xr.open_dataset(full_data, engine="cfgrib", backend_kwargs={'indexpath': ''})
    rh2 = ds['r2']
    # Select the first time slice if time is a dimension
    if 'time' in rh2.dims:
        data2d = rh2.isel(time=0).values
    else:
        data2d = rh2.values
    plt.figure(figsize=(10,8))
    im = plt.imshow(data2d, aspect='auto', origin='lower')
    plt.title('2D Image of r2 (first time slice)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar(im, label='r2 value')
    plt.tight_layout()
    plt.show()
    
print("Plotting complete.")

# %%
rh2.isel(x=[-130, -115, -100]).plot(y="latitude", hue="x")
#%%
rh2.isel(x=[-130, -115, -100]).plot(y="y", hue="x")

#%%
rh2.isel(y=[0, 30, 60, 90]).plot(x="longitude", hue="y")

#%%
rh2.T.plot.surface()

# %%
rh_gro = rh2.mean().groupby_bins("latitude", [0, 30, 60, 90]).mean()
rh_mn = rh2.mean()
rh_std = rh2.std()
rh_mn.plot.step()
(rh_mn + rh_std).plot.step(ls=":")
(rh_mn - rh_std).plot.step(ls=":")
plt.title('Zonal Mean Relative Humidity')

# %%
print(ds.longitude.attrs)
print(ds.latitude.attrs)

#%%
lat_bins = np.arange(0, 81, 2)
lat_center = np.arange(1, 80, 2)

rh2_lat_mean = ds.r2.groupby_bins('latitude', 
                    lat_bins, labels=lat_center).mean()
rh2_lat_mean.plot.line()
# %%
