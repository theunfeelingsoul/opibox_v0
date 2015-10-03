"""opibox_v0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
	# The next step is to point the root URLconf at the polls.urls module. 
	# In mysite/urls.py insert an include(), leaving you with:
    url(r'^polls/', include('polls.urls', namespace='polls')), #added this
	url(r'^kraken1/', include('kraken_1.urls', namespace='kraken_1')), #added this
    url(r'^admin/', include(admin.site.urls)),
]
