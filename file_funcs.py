"""

    Various useful functions to call 

    Liam.Buchart@nrcan-rncan.gc.ca
    July 16, 2025

"""

import subprocess

# run a CLI command
def execute_command(command):
    """
    Execute a CLI command and return output and error message
    Parameters:
    - command (str) 
    Returns:
    - output (str) 
    - error (str) and printed error message
    """

    try: 
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        output, error = process.communicate()

        output = output.decode("utf-8")
        error = error.decode("utf-8")

        return output, error
    
    except Exception as e:
        
        # if the exception occurs return the exceptions message as an error
        return None, str(e)