from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('beers/', views.BeerList.as_view(), name="beer_list"),
    path('beers/<int:pk>/', views.BeerDetail.as_view(), name="beer_detail"),
    path('beers/<int:pk>/update', views.BeerUpdate.as_view(), name="beer_update"),
    path('beers/new/', views.BeerCreate.as_view(), name="beer_create"),

    # User
    path('beers/favorite', views.FavoriteList.as_view(), name="favorite_list"),
    path('beers/favorite/new', views.FavoriteCreate.as_view(), name="favorite_create"),


    # Api
    path('breweries/', views.breweries, name='breweries'),
    path('breweries/<str:pk>/', views.BreweryDetail.as_view(),
         name="brewery_details"),
    path('results/', views.SearchResult.as_view(), name="search_results"),

    # Accounts/Signup
    path('accounts/signup/', views.Signup.as_view(), name="signup")

]
