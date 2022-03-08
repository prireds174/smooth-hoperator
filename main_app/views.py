from ast import BinOp
from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # def get(self, request):
    #     return HttpResponse("Smooth Hoperator")

class About(View):

    def get(self, request):
        return HttpResponse("Smooth Hoperator About")

class Beers:
    def __init__(self, name, image, type, description):
        self.name = name
        self.image = image
        self.type = type
        self.description = description