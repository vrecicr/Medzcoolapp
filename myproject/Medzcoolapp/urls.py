"""Medzcoolapp URL Configuration

***For further instructions, please reference 
"""
from django.conf.urls import url, include
from django.contrib import admin
from Medzcoolapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^home/$', views.home, name='home'),
	url(r'^chapters/$', views.chapters, name='chapters'),
	
	# These are added to test simple login and logout functionality.
	url(r'^login/$', auth_views.login, {'template_name': 'Medzcoolapp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
