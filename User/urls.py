'''
Created on Oct 13, 2015

@author: Nick
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),

    
    
]
