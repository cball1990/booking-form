from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import BookTable

def home(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['points'] and request.POST['gametype']:
            booktable = BookTable()
            booktable.name = request.POST['name']
            booktable.gametype = request.POST['gametype']
            booktable.points = request.POST['points']
            booktable.skilllevel = request.POST['skilllevel']
            booktable.opponent = request.POST['opponent']
            booktable.army = request.POST['army']
            booktable.save()

            return redirect('confirmed')
        else:
            return render(request, 'bookings/home.html', {'error':'All Fields Are Required'})
    else:
        return render(request, 'bookings/home.html')

def confirmed(request):
    return render(request, 'bookings/confirmed.html')

def admin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('seebookings')
        else:
            return render(request, 'bookings/admin.html', {'error':'Username or Password does not match'})

    return render(request, 'bookings/admin.html')

def seebookings(request):
    bookings = BookTable.objects.all()
    return render(request, 'bookings/seebookings.html', {'bookings':bookings})
