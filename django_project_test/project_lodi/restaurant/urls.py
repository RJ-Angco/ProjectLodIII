from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('addrestaurant/', views.addrestaurant, name='addrestaurant'),
    path('randomize_result/', views.randomize_result, name='randomize_result'),
    path('randomizeviabudget/', views.randomizeviabudget, name='randomizeviabudget'),
    path('addsuccess/', views.addsuccess, name='addsuccess'),
    path('randomizebudget_result/', views.randomizebudget_result, name='randomizebudget_result'),
]
