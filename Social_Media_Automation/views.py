from django.shortcuts import render
from django.template import Context, Template
from django.template.response import TemplateResponse



def welcome(request):

    return render(request, 'main.html')

