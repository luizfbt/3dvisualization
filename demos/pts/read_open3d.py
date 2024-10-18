import open3d as o3d
import os

this_path = os.path.abspath(os.path.dirname(__file__))
pts_file = os.path.join(this_path, 'bunnyData.pts')

# Load the .pts file
pcd = o3d.io.read_point_cloud(pts_file)

# Visualize the points
o3d.visualization.draw_geometries([pcd])
