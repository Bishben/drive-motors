from django.shortcuts import render
from django.http import HttpResponse
from home_page.models import car

# Create your views here.

def index(request):
    cars = car.objects.filter(featured = "Yes")
    dict = {"cars":cars}
    return render(request, "index.html", context=dict)

def home(request):
    cars = car.objects.filter(featured = "Yes")
    dict = {"cars":cars}
    return render(request, "home_page.html", context=dict)

def reachUs(request):
    return render(request, "reach_us.html")

def allCars(request):
    cars = car.objects.all()
    dict = {"cars":cars}
    return render(request, "allCars_page.html", context=dict)

def carPage(request):
    if request.method == "POST":
        car_name = request.POST.get('car_name')
        cars = car.objects.filter(name = car_name)
        dict = {"cars":cars}
        return render(request,"car_page.html", context=dict)

def filter(request):
    if request.method == "POST":
        car_make = request.POST.get('car_make')
        car_condition = request.POST.get('car_condition')
        car_price = request.POST.get('car_price')
        car_color = request.POST.get('car_color')
        if car_price == "Low to High":
            order = 'price'
        elif car_price == "High to Low":
            order = '-price'
        if car_color == "Any":
            cars = car.objects.filter(make = car_make,condition = car_condition).order_by(order)
            dict = {"cars":cars}
            return render(request,"search_page.html", context=dict)
        else:
            cars = car.objects.filter(make = car_make,condition = car_condition,color = car_color).order_by(order)
            dict = {"cars":cars}
            return render(request,"search_page.html", context=dict)
