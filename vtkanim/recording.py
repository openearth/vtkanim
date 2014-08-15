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
surface = envisage_engine.scenes[0].children[0].children[0].children[1]
surface.actor.actor.origin = array([ 0.,  0.,  0.])
surface.actor.actor.scale = array([ 1.,  1.,  8.])
surface.actor.actor.orientation = array([ 0., -0.,  0.])
surface.actor.actor.estimated_render_time = 3.0040740966796875e-05
surface.actor.actor.reference_count = 3
surface.actor.actor.allocated_render_time = 5000.000145999674
surface.actor.actor.render_time_multiplier = 0.5768508308021841
surface.actor.actor.position = array([ 0.,  0.,  0.])
surface.actor.actor.scale = array([ 1.,  1.,  8.])
surface.actor.actor.origin = array([ 0.,  0.,  0.])
surface.actor.actor.scale = array([  1.,   1.,  20.])
surface.actor.actor.orientation = array([ 0., -0.,  0.])
surface.actor.actor.estimated_render_time = 2.7179718017578125e-05
surface.actor.actor.allocated_render_time = 4998.502587919234
surface.actor.actor.render_time_multiplier = 0.5765053872174033
surface.actor.actor.position = array([ 0.,  0.,  0.])
surface.actor.actor.scale = array([  1.,   1.,  20.])
surface.actor.property.representation = 'wireframe'
surface.actor.property.specular_color = (0.6761120012207218, 1.0, 0.32054627298390176)
surface.actor.property.diffuse_color = (0.6761120012207218, 1.0, 0.32054627298390176)
surface.actor.property.ambient_color = (0.6761120012207218, 1.0, 0.32054627298390176)
surface.actor.property.color = (0.6761120012207218, 1.0, 0.32054627298390176)
surface.actor.property.line_width = 0.30000001192092896
surface.actor.property.line_width = 0.3
surface.actor.property.opacity = 0.4
scene = envisage_engine.scenes[0]
scene.scene.camera.position = [66017.450892770066, 333398.80098708876, 105042.13455783673]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.016479961166221614, 0.67522117395856063, 0.7374312016167901]
scene.scene.camera.clipping_range = [104299.48236577214, 221120.75588003555]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [65031.650732984039, 353334.25972589978, 86810.470539288639]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.016479961166221614, 0.67522117395856063, 0.7374312016167901]
scene.scene.camera.clipping_range = [77536.724455632444, 193682.1707499428]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64216.939857127822, 369809.84546045435, 71742.979614868731]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.016479961166221614, 0.67522117395856063, 0.7374312016167901]
scene.scene.camera.clipping_range = [55418.742711715255, 171005.65411350245]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [63543.625083692932, 383426.03201793751, 59290.507776505161]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.016479961166221614, 0.67522117395856063, 0.7374312016167901]
scene.scene.camera.clipping_range = [37139.41895641185, 152264.73127346917]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [62987.166593250877, 394679.07875965908, 48999.208736535278]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.016479961166221614, 0.67522117395856063, 0.7374312016167901]
scene.scene.camera.clipping_range = [22032.539819797486, 136776.36528997059]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [56614.326031022814, 382738.74189908395, 31178.384414387081]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [10865.899174602906, 150759.34754694189]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [57260.473161292102, 394111.0703969702, 25766.048933131904]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [137.95904508124053, 137959.04508124053]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [57794.479054076633, 403509.68899026461, 21293.044403168951]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [127.38028271289237, 127380.28271289237]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [58235.806238196084, 411277.14237315254, 17596.346444521881]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [118.63750389607569, 118637.50389607568]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
surface.actor.property.shading = True
surface.actor.property.frontface_culling = True
surface.actor.property.frontface_culling = False
surface.actor.property.backface_culling = True
surface.actor.property.edge_visibility = True
surface.actor.property.edge_visibility = False
surface.actor.property.ambient = 0.0221
surface.actor.property.color = (0.6761120012207218, 1.0, 0.3205462729839017)
surface.actor.property.ambient = 0.5525
surface.actor.property.color = (0.7539016839841822, 1.0, 0.5122971622027884)
surface.actor.property.ambient_color = (0.894697489890898, 1.0, 0.859357595178149)
surface.actor.property.color = (0.7192654242972526, 1.0, 0.7786739811684995)
surface.actor.property.diffuse_color = (0.6223392080567636, 1.0, 0.7340962844281681)
surface.actor.property.color = (0.7526569968446386, 1.0, 0.7940312235373432)
surface.actor.property.diffuse = 0.6022
surface.actor.property.specular_color = (0.4899977111467155, 0.8597695887693599, 1.0)
surface.actor.property.specular_power = 0.8305
surface.actor.property.specular_power = 3.9435
scene.scene.camera.position = [58600.539448212156, 417696.525334217, 14541.224164648273]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [111.41206685738415, 111412.06685738414]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [58901.971853184114, 423001.80050865043, 12016.329718471736]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [103.46974147484862, 103469.74147484862]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [59151.089543243586, 427386.32544619869, 9929.6400935324491]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [94.912377470669085, 94912.377470669089]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [58901.971853184114, 423001.80050865043, 12016.329718471736]
scene.scene.camera.focal_point = [60337.3642578125, 448265.015625, -6.977168083190918]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [103.46974147484862, 103469.74147484862]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [61129.553577069833, 422701.68890768901, 11651.677124363247]
scene.scene.camera.focal_point = [62564.94598169822, 447964.90402403858, -371.62976219168695]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [103.46974147484862, 103469.74147484862]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [62011.537121509544, 422407.83695561014, 11139.534112850615]
scene.scene.camera.focal_point = [63446.92952613793, 447671.05207195971, -883.77277370431989]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [103.46974147484862, 103469.74147484862]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [59206.228789236091, 422728.43638965866, 11478.264067448788]
scene.scene.camera.focal_point = [60641.621193864477, 447991.65150600823, -545.04281910614714]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025201623200538738, 0.430766193255191, 0.90211161445604371]
scene.scene.camera.clipping_range = [103.46974147484862, 103469.74147484862]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [58105.644997675357, 421528.31465402705, 8292.9957217346855]
scene.scene.camera.focal_point = [60641.621193864477, 447991.65150600823, -545.04281910614714]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.024259661941732562, 0.31877123424568332, 0.94752117075026687]
scene.scene.camera.clipping_range = [108.37712293189193, 108377.12293189194]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [63162.763625545944, 421549.17558879766, 9806.5422336118281]
scene.scene.camera.focal_point = [65698.739821735071, 448012.51244077884, 968.5036927709948]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.024259661941732562, 0.31877123424568332, 0.94752117075026687]
scene.scene.camera.clipping_range = [108.37712293189193, 108377.12293189194]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64343.118866187324, 421507.49518514442, 10020.430215942924]
scene.scene.camera.focal_point = [66879.095062376451, 447970.8320371256, 1182.3916751020902]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.024259661941732562, 0.31877123424568332, 0.94752117075026687]
scene.scene.camera.clipping_range = [108.37712293189193, 108377.12293189194]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64343.898774815993, 421497.24720901618, 9989.9689531327858]
scene.scene.camera.focal_point = [66879.87497100512, 447960.58406099735, 1151.9304122919507]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.024259661941732562, 0.31877123424568332, 0.94752117075026687]
scene.scene.camera.clipping_range = [108.37712293189193, 108377.12293189194]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64599.937359109972, 423291.84772345884, 14232.665477774539]
scene.scene.camera.focal_point = [66879.87497100512, 447960.58406099735, 1151.9304122919507]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.0093505286577899652, 0.46912382818506393, 0.88308289613309277]
scene.scene.camera.clipping_range = [104.79442553611351, 104794.4255361135]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64600.237963380379, 423276.76615625538, 14204.275800569205]
scene.scene.camera.focal_point = [66880.175575275527, 447945.5024937939, 1123.5407350866171]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.0093505286577899652, 0.46912382818506393, 0.88308289613309277]
scene.scene.camera.clipping_range = [104.79442553611351, 104794.4255361135]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [63170.934339897605, 422964.04687751445, 13365.399967501471]
scene.scene.camera.focal_point = [65450.871951792731, 447632.78321505297, 284.66490201887882]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.0093505286577899652, 0.46912382818506393, 0.88308289613309277]
scene.scene.camera.clipping_range = [104.79442553611351, 104794.4255361135]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [62692.147441399626, 417783.61224663135, 16112.354331252816]
scene.scene.camera.focal_point = [65450.871951792731, 447632.78321505297, 284.66490201887882]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.0093505286577899652, 0.46912382818506393, 0.88308289613309277]
scene.scene.camera.clipping_range = [112.87769233513232, 112877.69233513232]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64345.497512338829, 419627.41004630318, 19352.348089084531]
scene.scene.camera.focal_point = [65450.871951792731, 447632.78321505297, 284.66490201887882]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.031031192197041875, 0.56336045158302051, 0.82562828603615879]
scene.scene.camera.clipping_range = [104.44040065470385, 104440.40065470384]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.save(u'/Users/baart_f/data/megapex/grid00.png')
scene.scene.camera.position = [64537.339357259989, 424487.84671238629, 16043.080759071256]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.031031192197041875, 0.56336045158302051, 0.82562828603615879]
scene.scene.camera.clipping_range = [98.468965085157635, 98468.96508515763]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64695.88633648635, 428504.73651870928, 13308.149081396377]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.031031192197041875, 0.56336045158302051, 0.82562828603615879]
scene.scene.camera.clipping_range = [90.576603897472992, 90576.603897472989]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64826.916897830451, 431824.48016029852, 11047.874967615486]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.031031192197041875, 0.56336045158302051, 0.82562828603615879]
scene.scene.camera.clipping_range = [83.504402241126286, 83504.402241126285]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64935.206617949545, 434568.06994673592, 9179.8798322593775]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.031031192197041875, 0.56336045158302051, 0.82562828603615879]
scene.scene.camera.clipping_range = [77.659607483814824, 77659.60748381482]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [65024.702254411604, 436835.49952230399, 7636.0821997336679]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.031031192197041875, 0.56336045158302051, 0.82562828603615879]
scene.scene.camera.clipping_range = [72.829198593474985, 72829.198593474983]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [65098.66559033066, 438709.40826244291, 6360.2163877289504]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.031031192197041875, 0.56336045158302051, 0.82562828603615879]
scene.scene.camera.clipping_range = [68.837125130384052, 68837.125130384055]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [66479.925393319369, 440070.90295659128, 7928.0942170487688]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.049712953337805427, 0.70665557676562252, 0.70580912299040066]
scene.scene.camera.clipping_range = [67.187821303435371, 67187.821303435368]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [66696.026616027943, 438482.90810222353, 9533.214373210647]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.049712953337805427, 0.70665557676562252, 0.70580912299040066]
scene.scene.camera.clipping_range = [71.179894766526175, 71179.89476652618]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [66957.509095505317, 436561.43432843854, 11475.409762166522]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.049712953337805427, 0.70665557676562252, 0.70580912299040066]
scene.scene.camera.clipping_range = [76.010303656866441, 76010.303656866439]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67273.902895672931, 434236.45106215874, 13825.466182803131]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.049712953337805427, 0.70665557676562252, 0.70580912299040066]
scene.scene.camera.clipping_range = [81.855098414177604, 81855.098414177599]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67273.902895672931, 434236.45106215874, 13825.466182803131]
scene.scene.camera.focal_point = [65450.871951849993, 447632.78321548528, 284.66490199220641]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [81.855098414177604, 81855.098414177599]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72106.225609247223, 436969.1709603995, 15878.442888165631]
scene.scene.camera.focal_point = [70283.194665424278, 450365.50311372604, 2337.6416073547075]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [81.855098414177604, 81855.098414177599]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71789.831809079609, 439294.1542266793, 13528.386467529022]
scene.scene.camera.focal_point = [70283.194665424278, 450365.50311372604, 2337.6416073547075]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [76.010303656865815, 76010.303656865814]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71528.349329602235, 441215.62800046429, 11586.191078573149]
scene.scene.camera.focal_point = [70283.194665424278, 450365.50311372604, 2337.6416073547075]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [71.179894766525777, 71179.894766525773]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71312.248106893661, 442803.62285483204, 9981.0709224112707]
scene.scene.camera.focal_point = [70283.194665424278, 450365.50311372604, 2337.6416073547075]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [67.187821303435044, 67187.821303435048]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71189.567798668693, 442418.73510412668, 9616.8063526972055]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [67.187821303435044, 67187.821303435048]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71010.971746843425, 443731.12754575291, 8290.2607690923469]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [63.888587036414506, 63888.587036414508]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70863.371704012621, 444815.74939833657, 7193.9421049561006]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [61.16194714631758, 61161.94714631758]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70741.388197540888, 445712.13109468669, 6287.8936221988715]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [58.908525749543351, 58908.525749543347]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70640.575382274998, 446452.94241398433, 5539.0932232259547]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [57.046194016672089, 57046.194016672089]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70557.259006022199, 447065.18317373446, 4920.2499182896599]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [55.507076882067636, 55507.076882067639]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70488.402496722352, 447571.16727270151, 4408.8091704084254]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053730470168978306, 0.706235875622098, 0.70593478775288387]
scene.scene.camera.clipping_range = [54.235079250162869, 54235.079250162868]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70712.370655864914, 447587.70437589235, 4384.5410798833491]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.052916410638563484, 0.70271213093589169, 0.70950371001191348]
scene.scene.camera.clipping_range = [59.323891582115685, 59323.891582115684]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70634.812228240364, 447396.6656210309, 4196.5562174860179]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.042238273665977065, 0.64715646901711721, 0.76118620116697822]
scene.scene.camera.clipping_range = [60.123461298765839, 60123.46129876584]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [70840.783557837858, 447540.28316565469, 4302.8175254971102]
scene.scene.camera.focal_point = [70160.51435719931, 449980.61536302068, 1973.3770376406414]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.073238121110342336, 0.67786863343825499, 0.73152600324033568]
scene.scene.camera.clipping_range = [63.017684509492305, 63017.684509492305]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72080.487047174218, 447727.04307242448, 4136.4359887868504]
scene.scene.camera.focal_point = [71400.21784653567, 450167.37526979047, 1806.9955009303824]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.073238121110342336, 0.67786863343825499, 0.73152600324033568]
scene.scene.camera.clipping_range = [63.017684509492305, 63017.684509492305]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72794.026426129858, 447846.4677380537, 4053.1700683798103]
scene.scene.camera.focal_point = [72113.75722549131, 450286.79993541969, 1723.7295805233421]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.073238121110342336, 0.67786863343825499, 0.73152600324033568]
scene.scene.camera.clipping_range = [63.017684509492305, 63017.684509492305]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72779.468665646797, 447906.77742290706, 4120.6020816321479]
scene.scene.camera.focal_point = [72099.199465008249, 450347.10962027306, 1791.1615937756792]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.073238121110342336, 0.67786863343825499, 0.73152600324033568]
scene.scene.camera.clipping_range = [63.017684509492305, 63017.684509492305]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72178.408202483159, 447108.45622128673, 2952.6823824182643]
scene.scene.camera.focal_point = [72099.199465008249, 450347.10962027306, 1791.1615937756792]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.018166760634297549, 0.33792647762533418, 0.94099716499455555]
scene.scene.camera.clipping_range = [58.537896036935336, 58537.896036935337]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72138.597281793263, 447119.81731987867, 2985.8634918043676]
scene.scene.camera.focal_point = [72099.199465008249, 450347.10962027306, 1791.1615937756792]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.022180679757988958, 0.34731591143884261, 0.93748582661653079]
scene.scene.camera.clipping_range = [57.4144559299462, 57414.455929946198]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72239.073673933031, 447325.25609981688, 3432.2334727291568]
scene.scene.camera.focal_point = [72099.199465008249, 450347.10962027306, 1791.1615937756792]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.006542539098317748, 0.47745859559477982, 0.87862989061083485]
scene.scene.camera.clipping_range = [57.403531961264044, 57403.531961264045]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72236.76431533882, 447375.14766632905, 3405.1389606206867]
scene.scene.camera.focal_point = [72099.199465008249, 450347.10962027306, 1791.1615937756792]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.006542539098317748, 0.47745859559477982, 0.87862989061083485]
scene.scene.camera.clipping_range = [57.303527185692964, 57303.527185692961]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71727.271962079714, 447140.53862659214, 3016.557984375343]
scene.scene.camera.focal_point = [71589.707111749143, 450112.50058053614, 1402.5806175303348]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.006542539098317748, 0.47745859559477982, 0.87862989061083485]
scene.scene.camera.clipping_range = [57.303527185692964, 57303.527185692961]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71735.669517638336, 446876.13578403654, 2382.9085037350251]
scene.scene.camera.focal_point = [71589.707111749143, 450112.50058053614, 1402.5806175303348]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.018875155892500134, 0.29063010561572589, 0.95664929321033099]
scene.scene.camera.clipping_range = [60.897011457492695, 60897.011457492692]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [72474.967530267619, 446834.48798862449, 2135.3411551644758]
scene.scene.camera.focal_point = [72329.005124378426, 450070.85278512409, 1155.0132689597858]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.018875155892500134, 0.29063010561572589, 0.95664929321033099]
scene.scene.camera.clipping_range = [60.897011457492695, 60897.011457492692]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [71306.04761312058, 446947.62333687727, 1964.5814428594222]
scene.scene.camera.focal_point = [72329.005124378426, 450070.85278512409, 1155.0132689597858]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.014725541616057672, 0.25540576664612397, 0.96672180734067414]
scene.scene.camera.clipping_range = [68.606310227586363, 68606.310227586364]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69898.446220228056, 447303.01234035927, 1557.0122879722671]
scene.scene.camera.focal_point = [70921.403731485902, 450426.2417886061, 747.44411407263078]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.014725541616057672, 0.25540576664612397, 0.96672180734067414]
scene.scene.camera.clipping_range = [68.606310227586363, 68606.310227586364]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68880.232096228705, 447594.80828972469, 1396.1313535303066]
scene.scene.camera.focal_point = [69903.189607486551, 450718.03773797152, 586.56317963066931]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.014725541616057672, 0.25540576664612397, 0.96672180734067414]
scene.scene.camera.clipping_range = [68.606310227586363, 68606.310227586364]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68795.098467935328, 447613.30225825787, 1359.9056491145029]
scene.scene.camera.focal_point = [69818.055979193174, 450736.5317065047, 550.33747521486555]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.014725541616057672, 0.25540576664612397, 0.96672180734067414]
scene.scene.camera.clipping_range = [68.606310227586363, 68606.310227586364]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68829.668640562726, 447614.09654344898, 1406.652240557989]
scene.scene.camera.focal_point = [69852.626151820572, 450737.3259916958, 597.08406665835116]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.014725541616057672, 0.25540576664612397, 0.96672180734067414]
scene.scene.camera.clipping_range = [68.606310227586363, 68606.310227586364]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68951.650192893037, 447591.88876581419, 1463.6126950949147]
scene.scene.camera.focal_point = [69852.626151820572, 450737.3259916958, 597.08406665835116]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725805, 0.26137856449708391, 0.96510869161885848]
scene.scene.camera.clipping_range = [67.233231434585676, 67233.231434585672]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.save(u'/Users/baart_f/data/megapex/grid01.png')
scene.scene.camera.position = [68951.650192888977, 447591.88876581221, 1463.6126951037677]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [67.233231434594799, 67233.231434594796]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68762.4452415142, 446931.34694837709, 1645.5837070754465]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [68.484228063629885, 68484.228063629882]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68951.650192888977, 447591.88876581221, 1463.6126951037681]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [67.233231434594899, 67233.231434594898]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68762.4452415142, 446931.34694837709, 1645.5837070754469]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [68.484228063629885, 68484.228063629882]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68533.507250350711, 446132.09134928056, 1865.7686315611782]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [69.99793398476227, 69997.933984762261]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68256.492281042898, 445164.99207437376, 2132.1923901889131]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [71.829518149332415, 71829.51814933242]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67921.304168180432, 443994.80195173656, 2454.5651381284724]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [74.045734988462527, 74045.734988462529]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68256.492281042898, 445164.99207437376, 2132.1923901889136]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [71.829518149332415, 71829.51814933242]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67921.304168180432, 443994.80195173656, 2454.5651381284729]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [74.045734988462527, 74045.734988462529]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67515.726551616855, 442578.87190334551, 2844.6361631353398]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [76.727357363809972, 76727.357363809977]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67024.977635574935, 440865.59654479235, 3316.622103393649]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [79.972120437980024, 79972.120437980018]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [66431.171447164204, 438792.53336094302, 3887.7250911062024]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [83.898283757725963, 83898.283757725963]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67024.977635574935, 440865.59654479235, 3316.6221033936486]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [79.972120437980024, 79972.120437980018]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [66431.171447164204, 438792.53336094302, 3887.7250911062024]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [83.898283757725963, 83898.283757725963]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [65712.665959187216, 436284.12690848537, 4578.7597062383929]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [88.648941374618673, 88648.941374618676]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64843.274318735064, 433248.95510101161, 5414.9115905483432]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [94.397237091058585, 94397.237091058589]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [63791.310433787963, 429576.39721396833, 6426.6553705633833]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [101.35267490795115, 101352.67490795115]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [62518.434133001967, 425132.60217064596, 7650.865344381582]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [109.76875466639117, 109768.75466639118]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [60978.253809050912, 419755.61016822589, 9132.1594127016033]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [119.95221117410355, 119952.21117410355]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [59114.635617070133, 413249.44984529761, 10924.525235368828]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [132.27419354843542, 132274.1935484354]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [56859.657604773391, 405376.99585455441, 13093.28788079617]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [143.67362955567489, 143673.62955567488]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [54131.134209894335, 395851.32652575511, 15717.490681763253]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [154.07773387963704, 154077.73387963703]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [56859.657604773398, 405376.99585455441, 13093.287880796168]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [143.67362955567489, 143673.62955567488]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [54131.134209894342, 395851.32652575511, 15717.490681763251]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [154.07773387963701, 154077.733879637]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [50829.620902090683, 384325.26663790795, 18892.776070933422]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [166.66670011163114, 166666.70011163113]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [54131.134209894342, 395851.32652575511, 15717.490681763249]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [154.07773387963701, 154077.733879637]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [50829.620902090683, 384325.26663790795, 18892.776070933418]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [166.66670011163114, 166666.70011163113]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [46834.789799648257, 370378.7341736129, 22734.871391829325]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [2490.9475028817396, 181899.34925234402]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [42001.044165692918, 353503.42989181587, 27383.806730113374]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [20468.474996142897, 200330.85471260673]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [36152.211948606964, 333084.31171084149, 33009.018489437069]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [42221.283262988698, 222632.9763195244]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [42001.044165692925, 353503.42989181587, 27383.806730113367]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [20468.474996142897, 200330.85471260673]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [36152.211948606971, 333084.31171084149, 33009.018489437061]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [42221.283262988698, 222632.9763195244]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [29075.124965932962, 308377.17871186248, 39815.52471821873]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [68542.181265872234, 249618.54346389486]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [20511.849716897414, 278481.54778309789, 48051.397255044554]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [100390.4678493613, 282271.07970858319]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [10150.286665564388, 242307.8343592927, 58016.803024603811]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [138926.89461538309, 321780.64856465603]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-2387.2046265485551, 198537.64111648843, 70074.944005770507]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [185555.97100226948, 369587.22688050428]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-17557.569090005243, 145575.70729269524, 84665.294592982216]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [241977.15343040202, 427433.18664268043]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-35913.710090787819, 81491.767365905514, 102319.61880350838]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [310246.78416844225, 497426.79795491369]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-58124.640701734737, 3950.2000544899493, 123681.35109824502]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [392853.0373614711, 582119.06764271599]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-84999.866740980506, -89875.096392322972, 149529.04717487641]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [492806.60372503597, 684596.7139649567]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-58124.640701734723, 3950.2000544899493, 123681.35109824501]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [392853.0373614711, 582119.06764271599]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-84999.866740980506, -89875.096392322972, 149529.04717487638]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [492806.60372503597, 684596.7139649567]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-117518.89024846791, -203403.70509296661, 180804.75942760031]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [613750.41902494966, 808594.66601486795]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-156866.90869252765, -340773.32162074529, 218648.37125339627]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.015699024911725833, 0.26137856449708402, 0.96510869161885859]
scene.scene.camera.clipping_range = [760092.4355378449, 958632.18799526058]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-258559.41305819567, -330264.00698649313, 87887.788015623824]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.041359409438368654, 0.12814150351496836, 0.99089310943604458]
scene.scene.camera.clipping_range = [751037.52619092655, 967274.79679983249]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-78418.491500001997, -204886.10592375716, 523675.28835487296]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [778015.36466281815, 939541.0810647381]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-52685.487610016935, -91100.221045868879, 432893.12066849007]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [631673.34814992291, 789503.55908434535]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-31418.542246392943, 2937.700340815587, 357866.53580371087]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [510729.53285000933, 665505.60703443422]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-13842.554342571442, 80654.990743034228, 295861.09376670321]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [410775.96648644446, 563027.9607121934]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [683.05549529755081, 144884.15636470244, 244616.9267939697]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [328169.71329341573, 478335.69102439098]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [12687.691724941353, 197966.11142393242, 202266.37557683451]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [259900.08255537541, 408342.07971215789]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [22608.878691589118, 241835.49577040345, 167265.92002548312]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [203478.90012724293, 350496.11994998169]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [30808.206763198832, 278091.18531294144, 138339.92370205224]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [156849.82374035657, 302689.54163413373]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [37584.510954611818, 308054.56510016299, 114434.14161657217]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [118313.39697433481, 263179.97277806076]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [43184.762352473794, 332817.68889125512, 94677.296917828324]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [86465.110390845803, 230527.43653337256]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [47813.069292855595, 353283.08045414119, 78349.32609242019]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [60144.212387962296, 203541.86938900198]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [51638.116351022371, 370196.62720032805, 64855.135327620068]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [38391.4041211164, 181239.74778208433]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [54799.312266862675, 384174.76500709401, 53702.911555057995]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [20413.876627855308, 162808.24232182169]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [57411.870874995162, 395726.94501268573, 44486.19769343645]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [5556.4158896230874, 147575.59318110888]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [59571.010220559197, 405274.20121565409, 36869.078799534349]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [134.98662694911474, 134986.62694911472]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [61355.422902843529, 413164.49559827254, 30573.939217797073]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [124.58252262515258, 124582.52262515257]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [62830.144127871899, 419685.40004671755, 25371.344522146432]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [115.98408929956415, 115984.08929956415]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [64048.92199979617, 425074.57727683743, 21071.67948441863]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [108.14547569877745, 108145.47569877745]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [65056.176439403003, 429528.4427562753, 17518.237304478294]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [97.962019191065181, 97962.019191065177]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [65888.618125028486, 433209.32331779425, 14581.508230147443]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [89.545939432625048, 89545.939432625048]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [66576.586460256163, 436251.3733686363, 12154.459408386407]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [82.590501615732705, 82590.501615732705]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67145.155332345152, 438765.46431974543, 10148.633935856626]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [76.84220589929258, 76842.205899292574]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [67615.04696217076, 440843.22543636459, 8490.9269337658989]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [72.091548282399984, 72091.548282399977]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68003.387152109281, 442560.38338398375, 7120.9211469140573]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [68.165384962653832, 68165.384962653829]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68324.329457843589, 443979.52218366897, 5988.684959433197]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [64.920621888483581, 64920.621888483576]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68589.57103283063, 445152.36416687991, 5052.9525730853793]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [62.238999513136335, 62238.999513136332]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68808.77894604305, 446121.65506209555, 4279.6200223847036]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [60.022782674006329, 60022.782674006325]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [68989.942510681416, 446922.72191764566, 3640.502211888278]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [58.191198509436163, 58191.198509436159]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69139.664464928006, 447584.76064124081, 3112.3056742879262]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [56.677492588303686, 56677.492588303685]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69263.401617197916, 448131.90008222853, 2675.779610155404]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [55.426495959268287, 55426.495959268286]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69365.663726511892, 448584.08143841673, 2315.014267897121]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [54.392614447669089, 54392.61444766909]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69450.17786644079, 448957.78503857227, 2016.8610924770528]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [53.538166917421897, 53538.166917421899]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69520.024263076251, 449266.63098911406, 1770.4535094852608]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [52.832011933745981, 52832.011933745984]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69577.748557816303, 449521.87557633867, 1566.8108789135317]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [52.248412773683334, 52248.412773683332]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69625.454586527077, 449732.82151619368, 1398.5111842261524]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [51.766099418260261, 51766.099418260259]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69664.881056535989, 449907.15700367716, 1259.4205274597234]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [51.367493339398081, 51367.493339398083]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69697.46491604748, 450051.23591895279, 1144.46957145441]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [51.038066827941627, 51038.066827941628]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69724.393725561109, 450170.30940265168, 1049.468781367374]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [50.765813512688084, 50765.813512688081]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69746.648940035186, 450268.7172404193, 970.95573170866669]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [50.540810772809913, 50540.810772809913]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69765.041679269954, 450350.04603196279, 906.06891380890875]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [50.354858095225346, 50354.858095225347]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69780.242290207781, 450417.2599092715, 852.44344447026572]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [50.20117819639416, 50201.178196394161]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69792.804778586156, 450472.80856820429, 808.12487476890783]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [50.074170015542343, 50074.170015542339]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69803.187000386461, 450518.71655079338, 771.49795766034765]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.969204576822193, 49969.204576822194]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69811.767348981753, 450556.65703227196, 741.22777823178558]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.882456280360032, 49882.456280360027]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69818.858546167947, 450588.01280208898, 716.21110101809791]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.810763473366258, 49810.763473366256]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69824.719039710253, 450613.92666144192, 695.53616117207503]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.751513219650967, 49751.513219650966]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69829.562422803079, 450635.34307413024, 678.44943402660147]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.702546067821558, 49702.54606782156]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69833.565218747564, 450653.04258874874, 664.3281719229044]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.662077347296488, 49662.077347296487]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69836.873314569442, 450667.67028678051, 652.65770737439436]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.628632123730178, 49628.632123730174]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69839.607278058596, 450679.75929341838, 643.01269535083236]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1262281586616357, 0.60107323977733507, 0.78916247527646122]
scene.scene.camera.clipping_range = [49.600991443093676, 49600.991443093677]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [69834.75345602684, 450679.5418802597, 641.06608535655505]
scene.scene.camera.focal_point = [69852.626151816512, 450737.32599169383, 597.08406666720396]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.11899881661086206, 0.57778980109863154, 0.80746407188903357]
scene.scene.camera.clipping_range = [52.840317096555935, 52840.317096555933]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
