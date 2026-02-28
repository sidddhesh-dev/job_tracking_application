from django.shortcuts import render,redirect
from .models import JobApplication

def home(request):
    return render(request, 'core/home.html')

def developer(request):
    return render(request, 'core/developer.html')

def information(request):
    return render(request, 'core/information.html')


def tracker(request):
    jobs = JobApplication.objects.all().order_by('-date_applied')
    return render(request, 'core/tracker.html', {'jobs': jobs})


def add_job(request):
    if request.method == "POST":
        JobApplication.objects.create(
            company=request.POST.get('company'),
            role=request.POST.get('role'),
            date_applied=request.POST.get('date'),
            status=request.POST.get('status')
        )
    return redirect('tracker')


def delete_job(request, id):
    JobApplication.objects.get(id=id).delete()
    return redirect('tracker')
