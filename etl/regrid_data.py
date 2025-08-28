"""

    Use xarray and xesmf to regrid onto a unfiorm grid
    Grid defined locally

    function to be called by other scripts

    Liam.Buchart@nrcan-rncan.gc.ca
    July 25, 2025

"""

import xarray as xr
import xesmf as xe
import numpy as np

# default nice grid to cover canada
default_lat_range = (41.0, 84.0)  # from 41 to 84 degrees latitude
default_lon_range = (-141.0, -52.0)  # from -141 to -52 degrees longitude
default_resolution = 0.1  # resolution in degrees

# define the uniformly spaced grid
def create_target_grid(lat_range, lon_range, resolution):
    """
    Create a target grid with specified latitude and longitude ranges and resolution.

    Parameters:
    lat_range (tuple): Tuple of (min_lat, max_lat).
    lon_range (tuple): Tuple of (min_lon, max_lon).
    resolution (float): Resolution in degrees.

    Returns:
    xarray.Dataset: The target grid dataset.
    """
    lat = np.arange(lat_range[0], lat_range[1], resolution)
    lon = np.arange(lon_range[0], lon_range[1], resolution)
    ds_out = xr.Dataset(
    {
        "lat": (["lat"], lat, {"units": "degrees_north"}),
        "lon": (["lon"], lon, {"units": "degrees_east"}),
    })

    return ds_out


def regrid_data(ds, target_grid):
    """
    Regrid the input dataset onto a target grid using xesmf.

    Parameters:
    ds (xarray.Dataset): The input dataset to be regridded.
    target_grid (xarray.Dataset): The target grid onto which the data will be regridded.

    Returns:
    xarray.Dataset: The regridded dataset.
    """
    regridder = xe.Regridder(ds, target_grid, 'convservative')
    regridded_ds = regridder(ds)
    return regridded_ds

# make a default grid
canada_ten_km = create_target_grid(default_lat_range, default_lon_range, default_resolution)