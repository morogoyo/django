from django.shortcuts import render
from django.http import HttpResponse
from . import views 

def index(request):
	#return HttpResponse('<h1>test h1 hard coded</h1>')
	return render(request,'search/index.html')
