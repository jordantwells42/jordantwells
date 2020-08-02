from django.shortcuts import render

# Create your views here.
def webapps(request):
	return render(request, 'webapps/webapps_index.html')

