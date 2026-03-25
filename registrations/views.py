from django.shortcuts import redirect, get_object_or_404, render
from .models import Registration
from events.models import Event

def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if Registration.objects.filter(event=event).count() >= event.capacity:
        return render(request, 'full.html')

    Registration.objects.create(user=request.user, event=event)
    return redirect('/events/')


def mark_attendance(request):
    if request.method == 'POST':
        qr_data = request.POST['qr_data']
        user_id, event_id = qr_data.split('-')

        reg = Registration.objects.get(user_id=user_id, event_id=event_id)
        reg.attended = True
        reg.save()

        return render(request, 'success.html')
