from django.urls import path
from todoapp import views

urlpatterns = [
   
    path('home/', views.home , name = 'home-page' ),
    path('add/', views.add_task , name = 'addtask-page' ),
    path('delete_task/<int:pk>/', views.delete_task , name = 'delete-page' ),
]