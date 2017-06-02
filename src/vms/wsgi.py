"""
WSGI config for vms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vms.settings")
os.environ.setdefault("SECRET_KEY",
                      "gy%^a=g_#$%eon#pab)@m9o=7=qwzjd--@9d3t^de83b#qphg#")
os.environ.setdefault("DB_PWD", "TIFFsubIT")

application = get_wsgi_application()
