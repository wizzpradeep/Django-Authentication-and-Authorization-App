from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'home.html')

