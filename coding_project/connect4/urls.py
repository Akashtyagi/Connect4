
from  . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('START/',views.start, name='start'),
    path('MOVE/', views.move, name='move'), 
    path('ALL_MOVES/', views.all_moves, name='all_moves')
]