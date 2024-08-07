from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def payments(request):
    return render(request, 'payments.html')

def admin(request):
    return render(request, 'admin.html')
