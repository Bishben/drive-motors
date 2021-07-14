from django.conf.urls import url
from home_page import views

app_name = "web"

urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^reach_us/', views.reachUs, name = "reachUs"),
    url(r'^our_cars/', views.allCars, name = "allCars"),
    url(r'^car/$', views.carPage, name = "carPage"),
    url(r'^search-result/', views.filter, name = "search"),
]
