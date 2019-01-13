"""
Development configuration. The default configuration is extended,
 overriding any options that need to be changed in dev.
"""

import os

from .settings import *


SECRET_KEY = 'bic@058q(l6ff!9@*lwvbmolw9dw8f5+qp7pq$vv&ezxmisy1w'

DEBUG = True

RGBD_CONFIG_DIR = os.path.join(BASE_DIR, 'main/test/rgbd-config/')
