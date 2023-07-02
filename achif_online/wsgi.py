# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('/home/a/achifonlin/www/public_html')
sys.path.append('/home/a/achifonlin/www')
sys.path.append('/home/a/achifonlin/.djangovenv/lib/python3.8/site-packages/')
sys.path.remove('/usr/lib/python3.8/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "achif_online.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
