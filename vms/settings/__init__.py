import os

from vms.settings.base import *

environment = os.getenv('ENVIRONMENT')
if environment == 'production':
    from vms.settings.prod import *
if environment == 'development':
    from vms.settings.dev import *
