from django.urls import path
from .views import Calender, Login, BookAppointment

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('calender', Calender.as_view(), name='set-calender'),
    path('book-appointment', BookAppointment.as_view(), name='book-appointment'),
]