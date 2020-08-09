# -*- coding: utf-8 -*-

from django.urls import path
from .  import views


app_name = 'contact_us'

urlpatterns = [
    path('' , views.send_massage , name='us') , 

]