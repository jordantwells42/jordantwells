from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.webapps, name = 'webapps-index')
] 
urlpatterns += staticfiles_urlpatterns()
app_name = "webapps"