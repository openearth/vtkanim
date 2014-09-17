"""
VTK Animations

Usage:
  vtkanim <file> --type=<type>

Options:
  --type=<type> type that of grid (curvi, ugrid)
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
from tvtk.api import tvtk
import mayavi.mlab as mlab
mlab.options.offscreen = True
import docopt

import sources
# custom filter
from .filters import DataSetTriangleFilter
import pipes
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@mayavi2.standalone
def main():
    arguments = docopt.docopt(__doc__, version='0.1')
    
    if arguments['--type'] == 'curvi':
        import updates_d3d as updates
    else:
        import updates_fm as updates

    logger.info("%s", arguments)
    # load the source generator
    source_generator = getattr(sources, arguments['--type'] + '_from_file')
    # generate the vtksources
    grids = list(source_generator(arguments['<file>']))
    pipe_list = list(pipes.pipes[arguments['--type']])
    print arguments['--type']
    update_list = list(updates.updates[arguments['--type']])
    # # Setup the scen
    scene = mayavi.new_scene()
    scene.scene.background = (0.182, 0.182, 0.182)

    # scene.scene.camera.position = [58166.583048915491, 485959.0247321708, 16043.572309725338]
    # scene.scene.camera.focal_point = [69999.998654336974, 450767.75405880535, -1590.5715721476552]
    # scene.scene.camera.view_angle = 30.0
    # scene.scene.camera.view_up = [0.17119034045790907, -0.39476891515875417, 0.90269118249725122]
    # scene.scene.camera.clipping_range = [138.29111167241902, 138291.11167241901]
    # scene.scene.camera.compute_view_plane_normal()
    camera = scene.scene.camera

    #camera.position = [35000, 525000, 10000]
    #camera.focal_point = [60000, 450000, 0]
    #camera.view_angle = 30
    #camera.view_up = [0.17119034045790907, -0.39476891515875417, 0.90269118249725122]
    # bathymetry grid, waterlevel grid (different z's)
    # ug_bathy, ug_waterlevel = list(ugs)

    # wrap the sources in vtk
    for grid, pipe in zip(grids, pipe_list):
        vtkgrid = VTKDataSource(data=grid)
        # add the grid to the scen
        mayavi.add_source(vtkgrid)
        pipe(mayavi)
    scene.scene.isometric_view()
    mlab.view(azimuth=90, elevation=70, distance=50000)
    #camera.compute_view_plane_normal()
    scene.render()
    for t in range(75):
        logger.info("rendering %s", t)
        for grid, update in zip(grids, update_list):
            update(arguments['<file>'], grid, t)
        scene.render()
        mlab.savefig('test%03d.png' % (t, ))
    import sys
    sys.exit(0)
"""
import mayavi.mlab
recorder = mayavi.mlab.start_recording()
"""
