# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `DataSetTriangleFilter` class.
######################################################################
class DataSetTriangleFilter(FilterBase):

    """ Converts input shapes to triangles or tetras using
    the tvtk.DataSetTriangleFilter class.  This is useful when you have a
    downstream filter that only processes triangles or tetras."""

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.DataSetTriangleFilter, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])

