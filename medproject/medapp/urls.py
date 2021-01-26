from django.urls import path
from .views import Availability, Login

urlpatterns = [
    path('login', Login.as_view(), name='login'),
]