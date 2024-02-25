from django.urls import path
from . import views
app_name = 'registration'

urlpatterns = [
    path('new/', views.registration, name='registration-form'),
    path('list/', views.registration_list, name='registration-list')
]