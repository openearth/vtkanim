"""
Convert Delft3D output (NetCDF) file to a set of vtk files

Usage:
  d3d_to_vtk <file> [--scale_z=<sz>]

Options:
  --scale_z=<sz>  scale z of all grid points due to some instabilities in ParaView [default: 10]
"""

import logging
import docopt

import sources

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

arguments = docopt.docopt(__doc__)

sources.curvi_to_vtk(arguments['<file>'], int(arguments['--scale_z']))

