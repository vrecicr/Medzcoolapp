from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
#First view of the "home" page, referencing the index.html file.
def home(request):
	return render(request, 'Medzcoolapp/index.html')
def chapters(request):
	return render(request, 'Medzcoolapp/chapters.html')
