from django.shortcuts import render

from cars.models import Car
from core.models import Team


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)

    
    
    
    data = {
            'teams': teams,
            'featured_cars': featured_cars,

            
        }
    return render(request, 'home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
            'teams': teams,
            
        }
    return render(request,'about.html',data)


def service(request):
    return render(request,'service.html')


def contact(request):
    return render(request,'contact.html')
