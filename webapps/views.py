from django.shortcuts import render, redirect
from .models import WebApp
from .utils.lyric_cloud import *

# Create your views here.
def webapps(request):
	WebApps = WebApp.objects.all()
	context = {
		"WebApps" : WebApps
	}
	return render(request, 'webapps/webapps_index.html', context)

def lyric_cloud(request):
	print(request.method)
	if request.method == 'POST':
		login = user_login()
		return login

	else:
		code = request.GET.get("code", '')

		if code:
			tk = get_access_token(code)
			html_cloud = generate_lyric_cloud(tk)

			context = {
				'cloud' : html_cloud
			}
			return render(request, 'webapps/lyric_cloud.html', context)
		else:
			return render(request, 'webapps/lyric_cloud.html')


"""
def lyric_cloud_auth(request):
	spotify = None
	print(request.method)
	if request.method == 'POST':
		user_login()


	return render(request, 'webapps/lyric_cloud.html')	
"""