"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see

https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>> f47b2443b864e8feeb830dbc0ba208d9e982b145
"""

import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
