from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def jay(request):
	return render(request, 'index.html', {})