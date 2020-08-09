# -*- coding: utf-8 -*-

from django.urls import path
from .  import views, api


app_name = 'accounts'

urlpatterns = [
    path('signup/' , views.signup , name='signup') , 
    path('profile/' , views.profile , name='profile') ,
    path('profile_edit/' , views.profile_edit , name='profile_edit') ,

    #API urls
    path('api/profile/' , api.profile_api , name='profile_api') ,
    path('api/profile/<int:id>' , api.profile_details_api , name='profile_details_api') ,


    #class based views 
    path('api/v2/profile/' , api.ProfileApi.as_view() , name='ProfileApi') ,
    path('api/v2/profile/<int:id>' , api.ProfileDetails.as_view() , name='ProfProfileDetailsileApi') ,

]