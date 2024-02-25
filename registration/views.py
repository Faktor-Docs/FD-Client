from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return render(request, 'registration/registration.html')

def registration_list(request):
    return render(request, 'registration/registration-list.html')