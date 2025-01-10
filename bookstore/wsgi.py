"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
>>>>>>> 3e23122 (dcoker-networks)
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
>>>>>>> 3e23122 (dcoker-networks)

application = get_wsgi_application()
