from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.blog_index, name = 'blog_index'),
    path("post/<int:pk>/", views.post_detail, name = 'post_detail')
] 

urlpatterns += staticfiles_urlpatterns()
app_name = "blog"