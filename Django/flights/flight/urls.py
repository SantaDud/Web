from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= 'index'),
    path("<int:flight_id>", views.indFlight, name= "indiFlight"),
    path("<int:flight_id>/bkdel", views.bkdel, name = 'bkdel'),
]