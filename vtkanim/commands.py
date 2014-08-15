"""
VTK Animations

Usage:
  vtkanim <file>
"""

import logging

import numpy as np

from mayavi.sources.vtk_data_source import VTKDataSource
from mayavi.modules.outline import Outline
from mayavi.modules.surface import Surface
from mayavi.modules.vectors import Vectors
from mayavi.filters.cell_to_point_data import CellToPointData
from mayavi.filters.threshold import Threshold
from mayavi.scripts import mayavi2
import mayavi.mlab as mlab
import docopt

from .sources import ugrid_from_file

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@mayavi2.standalone
def main():
    arguments = docopt.docopt(__doc__, version='0.1')

    ugs = ugrid_from_file(arguments['<file>'])

    # Setup the scen
    scene = mayavi.new_scene()
    scene.scene.background = (0.182, 0.182, 0.182)
    scene.scene.camera.position = [71789.831809079609, 439294.1542266793, 13528.386467529022]
    scene.scene.camera.focal_point = [70283.194665424278, 450365.50311372604, 2337.6416073547075]
    scene.scene.camera.view_angle = 30.0
    scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
    scene.scene.camera.clipping_range = [76.010303656865815, 76010.303656865814]
    scene.scene.camera.compute_view_plane_normal()

    # bathymetry grid, waterlevel grid (different z's)
    ug_bathy, ug_waterlevel = list(ugs)

    # Generate grids
    src_bathy = VTKDataSource(data=ug_bathy)
    mayavi.add_source(src_bathy)
    surface_bathy = Surface()
    mayavi.add_module(surface_bathy)

    src_waterlevel = VTKDataSource(data=ug_waterlevel)
    mayavi.add_source(src_waterlevel)
    surface_waterlevel = Surface()
    mayavi.add_module(surface_waterlevel)
    module_manager_waterlevel = src_waterlevel.children[0]
    module_manager_waterlevel.scalar_lut_manager.data_range = np.array([-1,  1.])
    module_manager_waterlevel.scalar_lut_manager.use_default_range = False
    module_manager_waterlevel.scalar_lut_manager.lut_mode = 'gist_stern'

    surface_waterlevel.actor.actor.position = np.array([    0.,     0.,  1000.])
    surface_waterlevel.actor.actor.scale = np.array([   1.,    1.,  500.])

    surface_bathy.actor.actor.scale = (1.,  1.,  8.)
    surface_bathy.actor.property.representation = 'wireframe'
    surface_bathy.actor.property.color = (0.6761120012207218, 1.0, 0.32054627298390176)
    surface_bathy.actor.property.line_width = 0.30000001192092896
    surface_bathy.actor.property.line_width = 0.3
    surface_bathy.actor.property.opacity = 0.4
    surface_bathy.actor.property.shading = True
    surface_bathy.actor.property.frontface_culling = False
    surface_bathy.actor.property.backface_culling = True
    surface_bathy.actor.property.ambient = 0.5525
    surface_bathy.actor.property.ambient_color = (0.894, 1.0, 0.859)
    surface_bathy.actor.property.diffuse = 0.6022
    surface_bathy.actor.property.diffuse_color = (0.622, 1.0, 0.734)
    surface_bathy.actor.property.specular_power = 3.9435
    surface_bathy.actor.property.specular_color = (0.49, 0.86, 1.0)
    #surface_bathy.module_manager1.scalar_lut_manager.lut_mode = 'YlGnBu'
    logger.debug(dir(surface_bathy))

"""
import mayavi.mlab
recorder = mayavi.mlab.start_recording()
"""
