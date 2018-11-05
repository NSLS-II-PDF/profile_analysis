from xpdan.startup.analysis import start_analysis
from pyFAI.geometry import Geometry
from xpdtools.calib import _save_calib_param
from xpdan.pipelines.pipeline_utils import _timestampstr
import time

def calib_from_fit2d(directDist, centerX, centerY, 
                     tilt=0.0, tiltPlanRotation=0.0, 
                     pixelX=200, pixelY=200, splineFile=None):
    g = Geometry()
    g = g.setFit2D(directDist, centerX, centerY, tilt, tiltPlanRotation, 
                 pixelX, pixelY, splineFile))
    _save_calib_param(g, _timestampstr(time.time()),
                      os.path.join(glbl_dict['config_base'], glbl_dict['calib_config_name']))
