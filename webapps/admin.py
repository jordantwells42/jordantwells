from django.contrib import admin
from webapps.models import WebApp

class WebAppAdmin(admin.ModelAdmin):
    pass

admin.site.register(WebApp, WebAppAdmin)