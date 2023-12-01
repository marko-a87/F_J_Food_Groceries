import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir,"Database"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "F_J_app.settings")

application = get_wsgi_application()
from Database.models import 