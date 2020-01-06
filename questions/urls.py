from django.urls import path
from . import views

urlpatterns = [

    path('question/<int:id>/', views.single , name='question_single'),
    path('question/', views.home, name='question_home'),


]    
