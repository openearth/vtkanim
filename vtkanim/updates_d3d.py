import logging
import netCDF4
import numpy as np

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def waterlevel(filename, grid, t=0):
    """
    Generate an unstructured grid from filename.
    """
    ds = netCDF4.Dataset(filename)
    logging.info("rendering for t = %s", t)
    vars = {}
    thin = 1
    vars['s1'] = ds.variables['waterlevel'][t, 1:-1:thin, 1:-1:thin].ravel()
    vars['FlowElem_bl'] = ds.variables['depth'][1:-1:thin, 1:-1:thin].ravel()
    ds.close()
    data = vars['s1']
    # data = np.ma.masked_less_equal(vars['s1'], vars['FlowElem_bl']+0.2)
    # grid.cell_data.scalars = data.filled(np.nan)
    # grid.cell_data.scalars = data.filled(np.nan).copy()
    grid.cell_data.scalars = data.copy()
    grid.cell_data.scalars.name = 'water level (masked)'

    logger.info("min: %s max: %s", data.min(), data.max())
    grid.update()
    logger.info("range %s", grid.scalar_range )
    logger.info("count %s", len(data))


def salinity(filename, grid, t=0):
    """
    Generate an unstructured grid from filename.
    """
    ds = netCDF4.Dataset(filename)
    logging.info("rendering for t = %s", t)
    vars = {}
    thin = 1
    vars['sa1'] = ds.variables['suspsedconc'][t, 0, ::thin, 1:-1:thin, 1:-1:thin].squeeze().ravel()
    # vars['ucx'] = ds.variables['ucx'][t, ::thin,:]
    # vars['ucy'] = ds.variables['ucy'][t, ::thin,:]
    # vars['ucz'] = ds.variables['ucz'][t, ::thin,:]
    ds.close()

    grid.cell_data.scalars = vars['sa1'].T.flatten()
    grid.cell_data.scalars.name = 'salinity'
    # grid.cell_data.vectors = np.c_[vars['ucx'].T.flatten(), vars['ucy'].T.flatten(), vars['ucz'].T.flatten()]
    # grid.cell_data.vectors.name = 'velocity'

    grid.update()

def null(filename, grid, t=0):
    pass


updates = {'curvi': [waterlevel, salinity]}
