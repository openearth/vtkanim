"""
Convert Delft3D output file to vtk

Usage:
  d3d_to_vtk <file>
"""

import logging
import docopt

import sources

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

arguments = docopt.docopt(__doc__)
sources.curvi_to_vtk(arguments['<file>'])

