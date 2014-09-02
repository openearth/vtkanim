import numpy as np

from mayavi.modules.iso_surface import IsoSurface
from mayavi.modules.surface import Surface
from mayavi.filters.warp_scalar import WarpScalar
from mayavi.filters.cell_to_point_data import CellToPointData


def bathymetry(engine):
    cell_to_point_data = CellToPointData()
    engine.add_filter(cell_to_point_data)
    surface = Surface()
    engine.add_module(surface)
    module_manager = cell_to_point_data.children[0]
    module_manager.scalar_lut_manager.lut_mode = 'gist_earth'
    surface.actor.actor.scale = np.array([   1.,    1.,  100.])
    surface.actor.actor.position = np.array([    0.,     0.,  1000.])

def waterlevel(engine):
    cell_to_point_data = CellToPointData()
    engine.add_filter(cell_to_point_data)
    warp_scalar = WarpScalar()
    # use data as z
    # scale z
    warp_scalar.filter.normal = np.array([ 0.,  0.,  1.])
    # scale it up a bit
    warp_scalar.filter.scale_factor = 100.0
    engine.add_filter(warp_scalar)
    surface = Surface()
    engine.add_module(surface)
    # raise it a bit
    surface.actor.actor.position = np.array([    0.,     0.,  1000.])
    surface.actor.property.opacity = 0.7

    # color normal scale
    module_manager = warp_scalar.children[0]
    module_manager.scalar_lut_manager.lut_mode = 'YlGnBu'
    module_manager.scalar_lut_manager.data_range = np.array([-1.5,  1.5])

def salt(engine):
    cell_to_point_data = CellToPointData()
    engine.add_filter(cell_to_point_data)
    iso_surface = IsoSurface()
    engine.add_filter(iso_surface)
    module_manager = cell_to_point_data.children[0]
    module_manager.scalar_lut_manager.lut_mode = 'GnBu'
    iso_surface.contour.contours = [20, 25.0]
    iso_surface.actor.actor.position = np.array([    0.,     0.,  1000.])
    iso_surface.actor.actor.scale = np.array([   1.,    1.,  100.])


pipes = {}
pipes['ugrid'] = [bathymetry, waterlevel, salt]


# triangulate = DataSetTriangleFilter()
# triangulate.tetrahedra_only = True

# mayavi.add_filter(triangulate)
# add the requested modules
# surface = Surface()
# mayavi.add_module(surface)



# Generate grids
# src_bathy = VTKDataSource(data=ug_bathy)
# mayavi.add_source(src_bathy)
# surface_bathy = Surface()
# mayavi.add_module(surface_bathy)

# src_waterlevel = VTKDataSource(data=ug_waterlevel)
# mayavi.add_source(src_waterlevel)
# surface_waterlevel = Surface()
# mayavi.add_module(surface_waterlevel)
# module_manager_waterlevel = src_waterlevel.children[0]
# module_manager_waterlevel.scalar_lut_manager.data_range = np.array([-1,  1.])
# module_manager_waterlevel.scalar_lut_manager.use_default_range = False
# module_manager_waterlevel.scalar_lut_manager.lut_mode = 'gist_stern'

# surface_waterlevel.actor.actor.position = np.array([    0.,     0.,  1000.])
# surface_waterlevel.actor.actor.scale = np.array([   1.,    1.,  500.])

# surface_bathy.actor.actor.scale = (1.,  1.,  8.)
# surface_bathy.actor.property.representation = 'wireframe'
# surface_bathy.actor.property.color = (0.6761120012207218, 1.0, 0.32054627298390176)
# surface_bathy.actor.property.line_width = 0.30000001192092896
# surface_bathy.actor.property.line_width = 0.3
# surface_bathy.actor.property.opacity = 0.4
# surface_bathy.actor.property.shading = True
# surface_bathy.actor.property.frontface_culling = False
# surface_bathy.actor.property.backface_culling = True
# surface_bathy.actor.property.ambient = 0.5525
# surface_bathy.actor.property.ambient_color = (0.894, 1.0, 0.859)
# surface_bathy.actor.property.diffuse = 0.6022
# surface_bathy.actor.property.diffuse_color = (0.622, 1.0, 0.734)
# surface_bathy.actor.property.specular_power = 3.9435
# surface_bathy.actor.property.specular_color = (0.49, 0.86, 1.0)
# #surface_bathy.module_manager1.scalar_lut_manager.lut_mode = 'YlGnBu'
