from ast import BinOp
from re import template
from urllib import response
from .models import Beer
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from django.views.generic.base import TemplateView
import requests

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # def get(self, request):
    #     return HttpResponse("Smooth Hoperator")

class About(TemplateView):
    template_name = "about.html"

# class Beer:
#     def __init__(self, name, brand, image, type, description):
#         self.name = name
#         self.brand = brand
#         self.image = image
#         self.type = type
#         self.description = description

# beers = [
#     Beer("Silent Accord", "Six Bridges Brewing", "https://www.ajc.com/resizer/Do3KCvCWpdvpyOVZrk4gYm0NtrY=/814x458/cloudfront-us-east-1.images.arcpublishing.com/ajc/XRYGDKSF36SEKERV7VLENYYELY.jpg", "Coconut Milk Stout", "Jet black in color with a creamy, tan head, this milk stout is full of flavors. Aromas of coffee and dark chocolate come through from the use of roasted barley and chocolate malts. Smooth, dark chocolate and subtle notes of toasted coconut create a pleasant bouquet of flavors for the palate. A medium-light body that shows creaminess and low roast makes this offering approachable year round. At 6.5%, this beer is a real treat for those looking for rich, velvety smooth stout." ),
#     Beer("Neon Cylinders", "Creature Comforts Brewing Co.", "https://creaturecomfortsbeer.com/wp-content/uploads/2022/02/NeonCylinders-MagentaBeams_Can_for_web.jpg", "Sour Ale", "Neon Cylinders is an Intensely Fruited Sour Ale series. This version, 'Magenta Beams,' features prickly pear, passion fruit, Cara Cara orange, and grapefruit. This Neon Cylinders is rich in fruit flavor, and SUPER MAGENTA!" ),
#     Beer("Bestie", "Wild Heaven Beer", "https://static.spotapps.co/web/wildheavenbeer--com/custom/download/bestie_logo.jpg", "Pub Ale", "Bestie is a delicious session Pub Ale brewed in collaboration with England’s Arundel Brewery, Wild Heaven Beer and Robert Merrick of Atlanta’s 9 Mile Station. Built on the backbone of a traditional Standard Pub Ale with our own twist added, Bestie is designed to be a flavor-forward, yet easy-drinking beer. It is medium amber in color with light hints of peat and dark fruits and finishes crisp and clean with lingering floral hops.")
# ]

class BeerList(TemplateView):
    template_name = "beer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["beers"] = Beer.objects.filter(name__icontains=name)
            context["header"] = f"Being Poured: {name}"
        else:
            context["beers"] = Beer.objects.all()
            context["header"] = "The Brews"
        return context

class BeerDetail(DetailView):
    model = Beer
    template_name="beer_detail.html"


##API
def breweries(request):

    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=georgia')

    breweries = response.json()
        #print(breweries)

        #return HttpResponse("Breweries")
    return render(request, "breweries.html", {'breweries': breweries})
    pass

class BreweryDetail(TemplateView):
    template_name = "brewery_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        response = requests.get(f"https://api.openbrewerydb.org/breweries/{self.kwargs['pk']}")
        context[ 'brewery' ] = response.json()
        print(response.json())
        return context
        
       
