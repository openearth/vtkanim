import logging

import numpy as np
from tvtk.api import tvtk
import netCDF4
import osgeo.osr

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
CELLTYPES = {
    3: tvtk.Triangle().cell_type,
    4: tvtk.Quad().cell_type,
    6: tvtk.Wedge().cell_type,
    8: tvtk.Hexahedron().cell_type
}


def ugrid_from_file(filename):
    """
    Generate an unstructured grid from filename.
    """
    ds = netCDF4.Dataset(filename)
    logging.debug(ds.variables.keys())
    vars = {}
    dims = {}
    thin = 1
    vars['FlowElem_xcc'] = ds.variables['FlowElem_xcc'][::thin]
    vars['FlowElem_ycc'] = ds.variables['FlowElem_ycc'][::thin]
    vars['FlowElem_bl'] = ds.variables['FlowElem_bl'][::thin]
    vars['NetNode_x'] = ds.variables['NetNode_x'][::thin]
    vars['NetNode_y'] = ds.variables['NetNode_y'][::thin]
    vars['NetNode_z'] = ds.variables['NetNode_z'][::thin]
    vars['NetElemNode'] = ds.variables['NetElemNode'][::thin]
    vars['LayCoord_w'] = ds.variables['LayCoord_w'][:]
    vars['s1'] = ds.variables['s1'][30, ::thin]
    vars['sa1'] = ds.variables['sa1'][30, ::thin,:]
    vars['ucx'] = ds.variables['ucx'][30, ::thin,:]
    vars['ucy'] = ds.variables['ucy'][30, ::thin,:]
    vars['ucz'] = ds.variables['ucz'][30, ::thin,:]

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
    grid1.cell_data.scalars = vars['FlowElem_bl']
    grid1.cell_data.scalars.name = 'bathymetry'
    yield grid1

    points = points.copy()
    # Zet z to 0
    points[:, 2] = np.zeros_like(points[:,0])
    grid2 = tvtk.UnstructuredGrid(points=points)
    logger.debug("%s, %s, %s, %s", cell_types, offsets, cell_array, cells)
    grid2.set_cells(cell_types, offsets, cell_array)
    logger.debug("%s", grid2)
    grid2.cell_data.scalars = np.ma.masked_less_equal(vars['s1'], vars['FlowElem_bl']+0.2).filled(np.nan)
    grid2.cell_data.scalars.name = 'water level (masked)'
    yield grid2

    n_layers = vars['sa1'].shape[-1]
    logger.debug("n layers %s", n_layers)
    n_cells_per_layer = flowelemnode.shape[0]
    n_cells = n_cells_per_layer * n_layers
    n_points = vars['NetNode_x'].shape[0]
    # compute number of nodes per element
    elemtype = (~flowelemnode.mask).sum(1) * 2
    cell_types = np.array([CELLTYPES[type_] for type_ in elemtype])
    points = np.c_[vars['NetNode_x'], vars['NetNode_y'], np.zeros_like(vars['NetNode_x'])]
    points = np.array(wgs2rd.TransformPoints(points[:, :2]))
    logger.info("points.shape %s %s", points.shape, n_points)
    points = np.tile(points, [n_layers+1, 1])

    logger.info("points shape: %s", points.shape)
    for k in range(n_layers + 1):
        start = k*n_points
        end = (k+1)*n_points
        logger.info("updating from %s to %s with %s", start, end, k )
        # points run up to  1 meter below NAP
        points[start:end,2] = (0 - vars['NetNode_z'] - 1) * vars['LayCoord_w'][k] + vars['NetNode_z']

    cell_arrays = []
    for k in range(n_layers):
        # create a cell array for each layer
        cell_array = np.ma.hstack([
            elemtype[:,np.newaxis],
            flowelemnode - 1 + n_points*k,
            flowelemnode - 1 + n_points*(k+1)
        ])
        cell_arrays.append(cell_array[~cell_array.mask])
    cells = np.ma.vstack(cell_arrays).filled().ravel()

    logger.info("shapes done %s %s", cells.shape, cells.max())
    #offsets = np.r_[[0], np.cumsum(elemtype + 1)]

    offsets = np.concatenate([[0], np.cumsum(np.tile(elemtype + 1, [n_layers]))[:-1]])
    cell_types = np.array([CELLTYPES[type_] for type_ in elemtype])
    cell_types = np.tile(cell_types, [n_layers])

    cell_array = tvtk.CellArray()
    cell_array.set_cells(n_cells, cells)
    logger.info("arrays done")

    grid3 = tvtk.UnstructuredGrid(points=points)
    logger.debug("%s, %s, %s, %s %s", cell_types.shape, offsets.shape, cell_array, cells.shape, vars['sa1'])
    grid3.set_cells(cell_types, offsets, cell_array)
    logger.debug("%s", grid3)
    grid3.cell_data.scalars = vars['sa1'].T.flatten()
    grid3.cell_data.scalars.name = 'salinity'
    grid3.cell_data.vectors = np.c_[vars['ucx'].T.flatten(), vars['ucy'].T.flatten(), vars['ucz'].T.flatten()]
    grid3.cell_data.vectors.name = 'velocity'

    # TODO: add streamtracer here...
    yield grid3

def curvi_from_file(filename):
    """
    Generate an unstructured grid from filename.
    """
    ds = netCDF4.Dataset(filename)
    logging.debug(ds.variables.keys())
    vars = {}
    dims = {}

    # we have to squeeze out the nans
    thin = 1
    vars['LayerInterf'] = ds.variables['LayerInterf'][::thin].squeeze()
    vars['x'] = ds.variables['x'][1:-1:thin,1:-1:thin]
    vars['y'] = ds.variables['y'][1:-1:thin,1:-1:thin]
    vars['depth'] = ds.variables['depth'][1:-1:thin,1:-1:thin]
    vars['waterlevel'] = ds.variables['waterlevel'][-1,1:-1:thin,1:-1:thin]
    vars['suspsedconc'] = ds.variables['suspsedconc'][50,0,::thin,1:-1:thin,1:-1:thin].squeeze()

    x, y = vars['x'], vars['y']
    logger.debug("x: %s", x)

    n_cells = np.prod(x.shape)
    n_rows = x.shape[0]
    n_cols = x.shape[1]
    # compute number of nodes per element
    # quadruples all the way down
    elemtype = np.zeros(n_cells, dtype="int") + 4
    cell_types = np.array([CELLTYPES[type_] for type_ in elemtype], dtype="int")

    x_ll = x - np.gradient(x)[0]/2.0 - np.gradient(x)[1]/2.0
    x_lr = x - np.gradient(x)[0]/2.0 + np.gradient(x)[1]/2.0
    x_ur = x + np.gradient(x)[0]/2.0 + np.gradient(x)[1]/2.0
    x_ul = x + np.gradient(x)[0]/2.0 - np.gradient(x)[1]/2.0
    y_ll = y - np.gradient(y)[0]/2.0 - np.gradient(y)[1]/2.0
    y_lr = y - np.gradient(y)[0]/2.0 + np.gradient(y)[1]/2.0
    y_ur = y + np.gradient(y)[0]/2.0 + np.gradient(y)[1]/2.0
    y_ul = y + np.gradient(y)[0]/2.0 - np.gradient(y)[1]/2.0

    # cell matrices r,c,4
    cell_x = np.dstack([x_ll, x_lr, x_ur, x_ul])
    cell_y = np.dstack([y_ll, y_lr, y_ur, y_ul])


    # nodes
    # we need to append the last column because it is not repeated

    nodes_x = np.empty((x.shape[0]+1, x.shape[1]+1), dtype='double')
    nodes_y = np.empty_like(nodes_x)

    nodes_x[:-1,:-1] = x_ul
    nodes_x[-1,:-1] = x_ll[-1,:]
    nodes_x[:-1,-1] = x_ur[:,-1]
    nodes_x[-1,-1] = x_lr[-1,-1]
    nodes_y[:-1,:-1] = y_ul
    nodes_y[-1,:-1] = y_ll[-1,:]
    nodes_y[:-1,-1] = y_ur[:,-1]
    nodes_y[-1,-1] = y_lr[-1,-1]

    # nodes_x = nodes_x.ravel()
    # nodes_y = nodes_y.ravel()

    points = np.c_[nodes_x.ravel(), nodes_y.ravel(), np.zeros_like(nodes_x.ravel())]

    cells = []
    for i in range(n_rows):
        for j in range(n_cols):
            idx = np.ravel_multi_index([[i,i+1,i+1,i],[j, j,j+1,j+1]], nodes_x.shape)
            cells.extend(
                [4] + list(idx)
            )
    cells = np.array(cells)
    # cells = np.concatenate([
    #     # convert to vtk cell administration
    #     [4] + [i, i+(n_cols+1), i+1+(n_cols+1), i +1]
    #     for i in range(n_cells)
    # ])
    offsets = np.r_[[0], np.cumsum(elemtype + 1)]
    cell_array = tvtk.CellArray()
    cell_array.set_cells(n_cells, cells)

    grid1 = tvtk.UnstructuredGrid(points=points)
    logger.debug("%s, %s, %s, %s", cell_types, offsets, cell_array, cells)
    grid1.set_cells(cell_types, offsets, cell_array)
    grid1.cell_data.scalars = vars['waterlevel'].ravel()
    grid1.cell_data.scalars.name = 'water level'
    logger.debug("%s", grid1)
    logger.debug("%s", dir(grid1))
    grid1.build_links()
    yield grid1

    # we need to append the last column because it is not repeated
    n_layers = vars['LayerInterf'].shape[0] - 1
    n_cells = np.prod(x.shape)
    elemtype = np.zeros(n_cells * n_layers, dtype="int") + 8
    cell_types = np.array([CELLTYPES[type_] for type_ in elemtype], dtype="int")
    # nodes
    # we need to append the last column because it is not repeated
    logger.debug("%s", np.isnan(nodes_x).any())

    nodes_x = np.empty((x.shape[0]+1, x.shape[1]+1), dtype='double')
    nodes_y = np.empty_like(nodes_x)
    nodes_z = np.ones_like(nodes_x)

    nodes_x[:-1,:-1] = x_ll
    nodes_x[-1,:-1] = x_ul[-1,:]
    nodes_x[:-1,-1] = x_lr[:,-1]
    nodes_x[-1,-1] = x_ur[-1,-1]
    nodes_y[:-1,:-1] = y_ll
    nodes_y[-1,:-1] = y_ul[-1,:]
    nodes_y[:-1,-1] = y_lr[:,-1]
    nodes_y[-1,-1] = y_ur[-1,-1]


    logger.info("x shape %s", nodes_x.shape)
    nodes_x = np.repeat(nodes_x[:,:,np.newaxis], n_layers + 1, 2)
    nodes_y = np.repeat(nodes_y[:,:,np.newaxis], n_layers + 1, 2)
    depth = vars['depth']
    nodes_z = np.repeat(nodes_z[:,:,np.newaxis], n_layers + 1, 2)
    for i in range(n_layers + 1):
        nodes_z[:,:,i] += i
    logger.debug("%s, %s, %s", nodes_x.shape, nodes_y.shape, nodes_z.shape)
    points = np.c_[nodes_x.ravel(), nodes_y.ravel(), nodes_z.ravel()]
    step = x.shape[0]+1 * x.shape[1]+1
    cells = []
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(n_layers):
                idx = np.ravel_multi_index([
                    [i, i+1,i+1,i  , i, i+1 ,i+1,i  ],
                    [j, j  ,j+1,j+1, j, j   ,j+1,j+1],
                    [k, k  ,k  ,k  , k+1,k+1,k+1,k+1]
                ], nodes_x.shape)
                cells.extend(
                    [8] + list(idx)
                )
    offsets = np.r_[[0], np.cumsum(elemtype + 1)]
    cell_array = tvtk.CellArray()
    cell_array.set_cells(n_cells*n_layers, cells)

    grid2 = tvtk.UnstructuredGrid(points=points)
    #logger.debug("%s, %s, %s, %s", cell_types, offsets, cell_array, cells)
    #grid2.set_cells(cell_types, offsets, cell_array)
    grid2.set_cells(CELLTYPES[8], cell_array)
    grid2.cell_data.scalars = vars['suspsedconc'].ravel().copy()
    # grid2.cell_data.scalars = np.zeros(n_cells*n_layers)
    grid2.cell_data.scalars.name = 'supsended'
    logger.debug("%s", grid2)


    #file_name = 'grid2.vtu'
    #writer = tvtk.XMLDataSetWriter(file_name=file_name, input=grid2)
    #writer = tvtk.UnstructuredGridWriter(file_name=file_name, input=grid2)
    #writer.write()

    i = 0
    cell = grid2.get_cell(i)
    logger.debug("%s %s", i, cell)
    for i in range(8):
        logger.debug("%s %s %s", i, cell.get_point_id(i), points[cell.get_point_id(i)])

    grid2.build_links()
    yield grid2



