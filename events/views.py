from django.shortcuts import render, redirect
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        Event.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            date=request.POST['date'],
            capacity=request.POST['capacity'],
            created_by=request.user
        )
        return redirect('/events/')
    return render(request, 'create_event.html')
