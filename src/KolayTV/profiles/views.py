from datetime import time,datetime,timedelta 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from profiles.models import *
from django.views.generic.list_detail import object_list
from django import forms
