from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('beers/', views.BeerList.as_view(), name="beer_list"),
    path('beers/<int:pk>/', views.BeerDetail.as_view(), name="beer_detail"),
    # Api
    path('breweries/', views.breweries, name='breweries'),
    path('breweries/<str:pk>/', views.BreweryDetail.as_view(), name="brewery_details")

]
