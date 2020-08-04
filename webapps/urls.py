from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.webapps, name = 'webapps-index'),
    path("webapp/<int:pk>/", views.webapp_detail, name = 'webapp-detail')
] 
urlpatterns += staticfiles_urlpatterns()
app_name = "webapps"