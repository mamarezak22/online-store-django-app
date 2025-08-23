
import os
from celery import Celery
#proj is the name of your project
os.environ.setdefault("DJANGO_SETTINGS_MODULE","proj.settings")
#first arg is the app name
app = Celery("proj")
#all the variables that started with CELERY in settings.py are our celery configuration.
app.config_from_object("django.conf:settings",
						namespace = "CELERY")
						#you do not need attaching tasks to app. it discovers them in every dir that has a tasks.py file.
app.autodiscover_tasks()
						