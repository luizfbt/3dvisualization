import open3d as o3d
import os

this_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.abspath(os.path.join(this_path, '..', '..', 'data'))
obj_file = os.path.join(data_path, 'gralha_azul_torre.obj')

# Load .obj file
mesh = o3d.io.read_triangle_mesh(obj_file)

# Create a coordinate frame mesh
mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
    size=1.0,  # Adjust the size of the axes as needed
    origin=[0.0, 0.0, 0.0]  # Set the origin of the coordinate frame
)

# View the mesh
aabb = mesh.get_axis_aligned_bounding_box()
aabb.color = (1, 0, 0)
obb = mesh.get_oriented_bounding_box()
obb.color = (0, 1, 0)
o3d.visualization.draw_geometries([mesh, mesh_frame, aabb, obb])
