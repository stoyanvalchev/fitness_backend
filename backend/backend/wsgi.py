import os
import sys

# Path to your project directory
path = '/home/zarinkaranikolov/fitness_backend/backend'
if path not in sys.path:
    sys.path.append(path)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
