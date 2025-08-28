"""

    Various useful functions to call 

    Liam.Buchart@nrcan-rncan.gc.ca
    July 16, 2025

"""

import pandas as pd
import os
import json

def file_paths(link, variable):
    """
    Generate a list of file paths
    *** Note *** only grabbing output every 3 hours
    Input:
    link (str): The base URL or path where the files are located.
    variables (str): specific variable to extract

    Output:
    A dataframe of full file paths to extract variavles off the https server
    
    """

    # get the 0-48 every 3 hours
    forecast_hours = [x for x in range(0, 49, 3)]

    # initialize a dataframe to hold the file paths

