
"""
	urls.py for wisumUtleie-app. 
	  Relative urls
"""


from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.hey, name='Welcome message'),
	url(r'^scanner', views.scanner, name="Scanner view")
]