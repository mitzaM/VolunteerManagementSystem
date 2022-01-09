from dotenv import load_dotenv

from vms.settings.base import *

load_dotenv(os.path.join(BASE_DIR, '.env'))

environment = os.getenv('ENVIRONMENT')
if environment == 'production':
    from vms.settings.prod import *
if environment == 'development':
    from vms.settings.dev import *
