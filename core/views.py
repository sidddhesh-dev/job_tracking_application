from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def developer(request):
    return render(request, 'core/developer.html')