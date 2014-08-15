import logging

import numpy as np
from tvtk.api import tvtk
import netCDF4
import osgeo.osr

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
CELLTYPES = {
    3: tvtk.Triangle().cell_type,
    4: tvtk.Quad().cell_type
}
def ugrid_from_file(filename):
    """
    Generate an unstructured grid from filename.
    """
    ds = netCDF4.Dataset(filename)
    logging.debug(ds.variables.keys())
    vars = {}
    dims = {}
    for var in {
            'FlowElem_xcc', 'FlowElem_ycc', 'NetNode_x', 'NetNode_y',
            'NetNode_z', 's1', 'NetElemNode'
    }:
        # copy all the variables
        vars[var] = ds.variables[var][:]
        dims['nelem'] = len(ds.dimensions['nNetElem'])
    ds.close()
    vars['NetNode_z'] = np.ma.masked_less(vars['NetNode_z'], -100).filled(0)

    # reduce amount of cells
    index = np.logical_and.reduce([
        vars['FlowElem_xcc'] >= 4.16,
        vars['FlowElem_xcc'] < 4.2,
        vars['FlowElem_ycc'] >= 52.02,
        vars['FlowElem_ycc'] < 52.08
    ])
    # reduce amount of cells
    index = np.logical_and.reduce([
        vars['FlowElem_xcc'] < 4.2,
        vars['FlowElem_xcc'] >= 4.1,
        vars['FlowElem_ycc'] >= 51.98,
        vars['FlowElem_ycc'] < 52.08
    ])
    index = np.ones(vars['FlowElem_xcc'].shape, dtype='bool')
    cc = np.c_[
        vars['FlowElem_xcc'],
        vars['FlowElem_ycc'],
        np.zeros_like(vars['FlowElem_xcc'])
    ]
    points = np.c_[vars['NetNode_x'], vars['NetNode_y'], vars['NetNode_z']]

    wgs = osgeo.osr.SpatialReference()
    rd = osgeo.osr.SpatialReference()
    wgs.ImportFromEPSG(4326)
    rd.ImportFromEPSG(28992)
    wgs2rd = osgeo.osr.CoordinateTransformation(wgs, rd)
    points = np.array(wgs2rd.TransformPoints(points[:, :2]))
    points[:, 2] = vars['NetNode_z']
    cc = np.array(wgs2rd.TransformPoints(cc[:,:2]))
    cc[:,2] = 0

    # TODO: check where flowelemnode is
    flowelemnode = np.ma.masked_less(vars[u'NetElemNode'][index], 0)
    n_cells = index.sum()
    # compute number of nodes per element
    elemtype = (~flowelemnode.mask).sum(1)
    cell_types = np.array([CELLTYPES[type_] for type_ in elemtype])
    grid = tvtk.UnstructuredGrid()
    cells = np.concatenate([
        [n] + elem[~elem.mask].filled().tolist()
        for n, elem
        in zip(elemtype, flowelemnode-1)
    ])
    offsets = np.r_[[0], np.cumsum(elemtype + 1)]
    cell_array = tvtk.CellArray()
    cell_array.set_cells(n_cells, cells)

    grid1 = tvtk.UnstructuredGrid(points=points)
    logger.debug("%s, %s, %s, %s", cell_types, offsets, cell_array, cells)
    grid1.set_cells(cell_types, offsets, cell_array)
    logger.debug("%s", grid1)
    grid1.cell_data.scalars = vars['s1'][-1,:]
    grid1.cell_data.scalars.name = 'water level'
    yield grid1

    import scipy.interpolate
    interp = scipy.interpolate.LinearNDInterpolator(cc[:,:2], vars['s1'][-1,:])
    z = interp(points[:, :2])
    points[:, 2] = np.ma.masked_greater(z, 0.3).filled(np.nan)
    grid2 = tvtk.UnstructuredGrid(points=points)
    logger.debug("%s, %s, %s, %s", cell_types, offsets, cell_array, cells)
    grid2.set_cells(cell_types, offsets, cell_array)
    logger.debug("%s", grid2)
    grid2.cell_data.scalars = vars['s1'][-1, :]
    grid2.cell_data.scalars.name = 'water level'
    yield grid2


def mixed_type_ug():
    """A slightly more complex example of how to generate an
    unstructured grid with different cell types.  Returns a created
    unstructured grid.
    """
    points = np.array([
        [0, 0, 0],  [1, 0, 0],  [0, 1, 0],  [0, 0, 1],  # tetra
        [2, 0, 0],  [3, 0, 0],  [3, 1, 0],  [2, 1, 0],
        [2, 0, 1],  [3, 0, 1],  [3, 1, 1],  [2, 1, 1],  # Hex
    ], 'f')
    # shift the points so we can show both.
    points[:, 1] += 2.0
    # The cells
    cells = np.array([
        4, 0, 1, 2, 3,  # tetra
        8, 4, 5, 6, 7, 8, 9, 10, 11  # hex
    ])
    # The offsets for the cells, i.e. the indices where the cells
    # start.
    offset = np.array([0, 5])
    tetra_type = tvtk.Tetra().cell_type  # VTK_TETRA == 10
    hex_type = tvtk.Hexahedron().cell_type  # VTK_HEXAHEDRON == 12
    cell_types = np.array([tetra_type, hex_type])
    # Create the np.array of cells unambiguously.
    cell_array = tvtk.CellArray()
    cell_array.set_cells(2, cells)
    # Now create the UG.
    ug = tvtk.UnstructuredGrid(points=points)
    # Now just set the cell types and reuse the ug locations and cells.
    ug.set_cells(cell_types, offset, cell_array)
    return ug


def generate():
    # ----------------------------------------------------------------------
    # Create the unstructured grids and assign scalars and vectors.
    ug = mixed_type_ug()
    temperature = np.arange(0, 120, 10, 'd')
    velocity = np.random.randn(12, 3)
    a = np.array([1, 2], 'double')
    ug.cell_data.scalars = a
    ug.cell_data.scalars.name = 'a'
    ug.point_data.scalars = temperature
    ug.point_data.scalars.name = 'temperature'
    # Some vectors.
    ug.point_data.vectors = velocity
    ug.point_data.vectors.name = 'velocity'
    return ug
