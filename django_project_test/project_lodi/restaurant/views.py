from django.shortcuts import render
from .models import Restaurant
from .forms import RestaurantForm
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.db.models import Max
from django.core.exceptions import *
import random

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def addrestaurant(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('addsuccess')
    else:
        form = RestaurantForm()
    return render(request, 'addrestaurant.html', {'form': form})

def randomize_result(request):
    obj = get_random()
    context = {
        'object' : obj
    }
    return render(request, 'randomize_result.html', context)

def get_random():
    max_id = Restaurant.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        restaurant = Restaurant.objects.filter(pk=pk).first()
        if restaurant:
            return restaurant

def get_randombudget(max_budget):
    max_id = Restaurant.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        restaurant = Restaurant.objects.filter(pk=pk, min_price__lte = max_budget).first()
        if restaurant:
            return restaurant

def randomizeviabudget(request):
    return render(request, 'randomizeviabudget.html', {})

def addsuccess(request):
    return render(request, 'addsuccess.html', {})

def randomizebudget_result(request):
    if request.method == "POST":
        max_budget = request.POST.get('inputBudget', None)
        restaurant = get_randombudget(max_budget)
        context = {
            'object': restaurant
        }
        return render(request, 'randomizebudget_result.html', context)

    else:
        return render(request, 'randomizeviabudget.html', {})
