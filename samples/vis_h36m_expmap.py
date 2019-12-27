import sys
sys.path.insert(0, './..')
import mocap.datasets.h36m as H36M
from os.path import isdir
from os import makedirs
from mocap.visualization.sequence import SequenceVisualizer
import mocap.processing.normalize as norm
import mocap.math.fk as FK

vis_dir = '../output/'
if not isdir(vis_dir):
    makedirs(vis_dir)

vis = SequenceVisualizer(vis_dir, 'vis_h36m_expmap', to_file=True, mark_origin=True)


Seq = H36M.get_euler('S1', 'walking', 1)[0:250:5]
Seq = FK.euler_fk(Seq)

Seq_xyz = norm.remove_rotation_and_translation(H36M.get3d('S1', 'walking', 1)[0:250:5])


vis.plot(Seq, Seq_xyz, parallel=True, create_video=True)