"""
WSGI config for outfit_matcher project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'outfit_matcher.settings')

application = get_wsgi_application()