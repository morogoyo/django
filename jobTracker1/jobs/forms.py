#-*- coding: utf-8 -*-
from django import forms

class Search(forms.Form):   
   search = forms.CharField(max_length = 100)