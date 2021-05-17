from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "flight/index.html",{
        "flights": Flight.objects.all()
    })

def indFlight(request, flight_id):
    return render(request, 'flight/indFlight.html', {
        'flight': Flight.objects.get(pk = flight_id),
        'passenger':  Flight.objects.get(pk = flight_id).Passenger.all(),
        'not_passenger': Passenger.objects.exclude(flights= Flight.objects.get(pk = flight_id)).all()
    })

def bkdel(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        if 'passenger' in request.POST:    
            passenger = Passenger.objects.get(pk = int(request.POST['passenger']))
            passenger.flights.add(flight)
        elif 'delete' in request.POST:
            passenger = Passenger.objects.get(pk = int(request.POST['delete']))
            passenger.flights.remove(flight)
        return HttpResponseRedirect(reverse('indiFlight', args = (flight.id,)))