from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.webapps, name = 'webapps-index'),
    path("lyric-cloud/", views.lyric_cloud, name = "lyric_cloud"),
   # path("lyric-cloud/authenticate/", views.lyric_cloud_auth, name = "lyric_cloud_auth")
] 
urlpatterns += staticfiles_urlpatterns()
app_name = "webapps"