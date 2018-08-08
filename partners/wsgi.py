"""
WSGI config for partners project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "partners.settings")

application = get_wsgi_application()
