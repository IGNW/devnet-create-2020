import sys
import os

def pre():

    # Change directory and path into the imported repo
    original_dir = os.getcwd()
    working_dir = original_dir + "/repos/cucm_axl_zeep"
    sys.path.append(original_dir + "/repos/cucm_axl_zeep")
    os.chdir(working_dir)

    # Run the script and define all the variables you want returned from the script
    from test_pull_regions import cucm_device_pools, cucm_regions 

    # Return the current directory to its original value
    os.chdir(original_dir)

    # Pass all the defined variables back to the gui
    return locals()

def main(**kwargs):
    print(locals())
    return {'some': 'value'}

if __name__ == "__main__":
    vars = pre()
    main(**vars)
