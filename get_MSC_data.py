"""

    Get select data from the MSC DataMart
    Initial use is for VPD and HWD Index.
    Extensions include: wind shift map, prob of crossover
    wind accumulation (monthly), and dry lightning possibility

    Liam.Buchart@nrcan-rncan.gc.ca
    July 16, 2025

    virtualenv is at ./ENV/Scriptss/activate

"""

import subprocess
import os
from pathlib import Path

from file_funcs import execute_command

##### USER INPUTS #####
link = "https://dd.weather.gc.ca/model_gem_regional/10km/grib2/"  # link to RDPS data
text_file = "variable_list.txt"  # name of the txt file to read and write to
model_run = "12"  # one of four daily model runs [00, 06, 12, 18]
forecast_hour = "08"  # how many hours into the future (from the model run time)
save_dir = "./RDPS/"

# create the production run date
year = "2025"
month = "07"
day = "02"
hour = "12"  # one of four daily model runs [00, 06, 12, 18] - same as model run I believe (unsure)
fsct_hr = ["009"]  # number of hours from forecast initial time - need three digist for the ECCC convention

# which variable would you like??
vars = ["TMP_TGL", "TMP_ISBL"]
##### END USER INPUTS #####

# generate a text file of deisred dates and times to download
all_vars = []
count = 0

for var in vars:
    for hh in fsct_hr:

        # concetenate strings to match MSC naming convention
        all_vars.append("*" + var + "*" + year + month + day + hour + "_P" + hh + ".grib2")
        count += 1

# save the variables to a txt file that will be later read by our wget command
with open(text_file, "w") as file:

    for line in all_vars:
       file.write(line + "\n")  # new line for each value save so we can see what we grabbed later

# define current working directory path
cwd = Path.cwd()

# execute the wget command following: https://eccc-msc.github.io/open-data/msc-datamart/readme_wget-datamart_en/
for var in all_vars:
    print("Variable: ", var)
    print("Save directory: ", save_dir)
    print("link: ", link)
    print("command: ", f"wget -nd -r -l1 -A {var} {link}")

    output, error = execute_command(f"wget -nd -r -l1 -A {var} {link}")

    if error: 
        print(f"Error getting MSC Data: {all_vars}")
        print(f"Error: {error}")
    else:
        print(f"MSC Data successfully downloaded")
        print(f"Output: {output}")

        # save the variable
        os.rename(str(cwd) + "/" + "*" + var + "*" + year + month + day + hour + "_P" + hh + ".grib2", 
                    str(cwd) + save_dir + "*" + var + "*" + year + month + day + hour + "_P" + hh + ".grib2")
        
print("Your data has been aquired my leige ")
