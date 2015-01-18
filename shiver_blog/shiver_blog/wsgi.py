"""
WSGI config for shiver_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shiver_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
