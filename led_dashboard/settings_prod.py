"""
Development configuration. The default configuration is extended,
 overriding any options that need to be changed in dev.
"""

from led_dashboard.settings_prod import *

DEBUG = False

RGBD_CONFIG_DIR = os.path.join(os.environ.get('HOME'), '.config/rgbd/')
