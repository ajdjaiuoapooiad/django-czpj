
from django.urls import include, path

from contacts import views



urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),
]

