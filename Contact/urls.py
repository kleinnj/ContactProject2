'''
Created on Oct 14, 2015

@author: Nick
'''

from django.conf.urls import include, url
from . import views
urlpatterns = [
               
   url(r'^$S', views.IndexView.as_view(), name='index'),
     
   

]
