from django.shortcuts import render
from .models import WebApp

# Create your views here.
def webapps(request):
	WebApps = WebApp.objects.all()
	context = {
		"WebApps" : WebApps
	}
	return render(request, 'webapps/webapps_index.html', context)

