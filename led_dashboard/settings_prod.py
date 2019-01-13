"""
Production configuration. The default configuration is extended,
 overriding any options that need to be changed in prod.

https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
"""

import os

from .settings import *

# Alright look... I -know- this is not supposed to be saved to version control.
#  We don't save passwords. We don't give session tokens. We don't use CSRF.
#  I'm fine with keeping this secret public. If you're so concerned, change it yourself.
SECRET_KEY = '8quh@_&lwdkc#*tppd&@jfxfv#f39=hrxt979i-ulh=s7&_^oc'

DEBUG = False
