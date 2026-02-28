from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('developer/', views.developer, name='developer'),
    path('information/', views.information, name='information'),
    path('tracker/', views.tracker, name='tracker'),
    path('add-job/', views.add_job, name='add_job'),
    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),
]