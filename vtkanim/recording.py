# Recorded script from Mayavi2
from numpy import array
try:
    engine = mayavi.engine
except NameError:
    from mayavi.api import Engine
    engine = Engine()
    engine.start()
if len(engine.scenes) == 0:
    engine.new_scene()
# -------------------------------------------
from mayavi.filters.threshold import Threshold
threshold = Threshold()
mayavi.add_filter(threshold, ug_waterlevel)
surface_waterlevel = Surface()
mayavi.add_filter(surface2, threshold)
threshold.auto_reset_lower = False
threshold.auto_reset_upper = False

module_manager2 = threshold.children[0]
module_manager2.vector_lut_manager.data_range = array([ 0.,  1.])
