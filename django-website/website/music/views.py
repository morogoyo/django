from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Album
# Create your views here.


def index(request):
	return HttpResponse("<h1>This is the music{%{{album_title}}%} app homepage</h1>")


   

