"""

    Create a variety of wind shift products from raw model output

    Liam.Buchart@nrcan-rncan.gc.ca
    July 24, 2025

"""

#%%
import xarray as xr
import numpy as np
import cfgrib
import matplotlib.pyplot as plt
import cartopy.feature as cfeature

from cartopy import crs as ccrs
from pathlib import Path

from etl.regrid_data import regrid_data, canada_ten_km

##### USER DEFINED VARIABLES #####
data_dir = "RDPS"
save_dir = "/FIGURES/"
# consult the variable list or any data directory (RDPS, HRDPS, etc.) for names/conventions
raw_speed = "WindSpeed_AGL-10m"
raw_dir = "WindDir_AGL-10m"
wind_comps = ["si10", "wdir10"]  # this is stupid
year = "2025"
month = "07"
day = "02"
model_run = "12"
fcst_hr = "008"
##### END USER DEFINED VARIABLES #####

# define the path to the data
spd_file = f"\\{year}{month}{day}T{model_run}Z_MSC_{data_dir}_{raw_speed}_RLatLon0.09_PT{fcst_hr}H.grib2"
dir_file = f"\\{year}{month}{day}T{model_run}Z_MSC_{data_dir}_{raw_dir}_RLatLon0.09_PT{fcst_hr}H.grib2"

p = Path(data_dir).resolve()
sp = Path(save_dir).resolve()

#%%
# quick map of the speed and direction data
# from a dataset
def quick_ds_map(ds, var_name, title):
    plt.figure(figsize=(10, 8))
    # data resolution
    resol = '50m'
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-145, -45, 43, 75], crs=ccrs.PlateCarree())
    # province boundaries
    provinc_bodr = cfeature.NaturalEarthFeature(category='cultural', 
                    name='admin_1_states_provinces_lines', scale=resol, facecolor='none', edgecolor='k')
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle='-')
    ax.add_feature(provinc_bodr, linestyle='--', linewidth=0.6, edgecolor="k", zorder=10)
    ax.set_title(title)
    ds[var_name].plot.pcolormesh(ax=ax, 
                                 transform=ccrs.PlateCarree(), 
                                 x="longitude", y="latitude")
    plt.colorbar(label=var_name)
    plt.show()

#%%
# quick map from a data array
def quick_da_map(da, var_name, title):
    plt.figure(figsize=(10, 8))
    # data resolution
    resol = '50m'
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-145, -45, 43, 75], crs=ccrs.PlateCarree())
    # province boundaries
    provinc_bodr = cfeature.NaturalEarthFeature(category='cultural', 
                    name='admin_1_states_provinces_lines', scale=resol, facecolor='none', edgecolor='k')
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle='-')
    ax.add_feature(provinc_bodr, linestyle='--', linewidth=0.6, edgecolor="k", zorder=10)
    ax.set_title(title)
    da.plot.pcolormesh(ax=ax, 
                                 transform=ccrs.PlateCarree(), 
                                 x="longitude", y="latitude")
    plt.colorbar(label=var_name)
    plt.show()

#%%
# open the datasets using xarray and cfgrib
# backend_kwargs={'indexpath': ''} is used to avoid creating an index file
spd = xr.open_dataset(f"{data_dir}{spd_file}", 
                      engine="cfgrib", backend_kwargs={'indexpath': ''})
dir = xr.open_dataset(f"{data_dir}{dir_file}", 
                      engine="cfgrib", backend_kwargs={'indexpath': ''})


# %%
quick_ds_map(spd, wind_comps[0], 
          f"{wind_comps[0]} at {year}-{month}-{day} {model_run}:{fcst_hr}")

#%%
quick_ds_map(dir, wind_comps[1], 
          f"{wind_comps[1]} at {year}-{month}-{day} {model_run}:{fcst_hr}")

#%%
# get wind speed and direction differences from adjacent grid points
spd_diff_lon_up = spd[wind_comps[0]].diff('longitude', label='upper')
spd_diff_lon_lo = spd[wind_comps[0]].diff('longitude', label='lower')

spd_diff_lat_up = spd[wind_comps[0]].diff('latitude', label='upper')
spd_diff_lat_lo = spd[wind_comps[0]].diff('latitude', label='lower')

# %%

