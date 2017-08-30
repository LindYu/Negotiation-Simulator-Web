# Survey/urls.py
from django.conf.urls import url
from Survey import views
from django.contrib import admin
urlpatterns = [
	url(r'^$',views.get_User_Info,name = 'home'),
    url(r'^vote/$', views.get_SenarioChoice, name = 'vote'),
	#url(r'^edit/$',admin.get_edit,name = 'add'),
	]