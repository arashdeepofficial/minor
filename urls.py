from django.contrib import admin
from django.urls import path
from users.views import signup
from events.views import event_list, create_event
from registrations.views import register_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('events/', event_list),
    path('create/', create_event),
    path('register/<int:event_id>/', register_event),
]
