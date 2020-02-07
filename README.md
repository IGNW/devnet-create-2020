# Building the Container
Using the standard library argparse control the container
* ./dock.py build - Build the initial container image
* ./dock.py rebuild - Force a rebuild of the container image using the no-cache setting
* ./dock.py start - Start the container
* ./dock.py stop - Stop the container
* ./dock.py delete - Delete the container (not the image)
* ./dock.py restart - Stop and start the running container