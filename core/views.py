from django.shortcuts import render

from core.models import Team


def home(request):
    teams = Team.objects.all()
    data = {
            'teams': teams,
            
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
