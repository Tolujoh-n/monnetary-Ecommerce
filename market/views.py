from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.response import TemplateResponse

# Create your views here.
class home(TemplateView):
    template_name = "base.html"
