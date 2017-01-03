from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('<h1>This is the jobs page</h1>')

def started(request):
	return HttpResponse('<h1>this page are all the started jobs for lms</h1>')