import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

#os.environment.setdefault("DJANGO_SETTING_MODULE","polls.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)