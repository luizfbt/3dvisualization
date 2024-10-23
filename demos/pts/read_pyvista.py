import os
import pyvista as pv

this_path = os.path.abspath(os.path.dirname(__file__))
pts_file = os.path.join(this_path, 'bunnyData.pts')

# Load the .pts file
points = pv.read(pts_file)

# Visualize the points
points.plot(point_size=1)
