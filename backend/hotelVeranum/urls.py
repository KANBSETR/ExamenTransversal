from django.contrib import admin
from django.urls import path
from hotelVeranum import views


urlpatterns = [
    path('habitacion/', views.HabitacionList.as_view(), name='habitacion-list'),
    path('habitacion/<int:pk>/', views.HabitacionDetail.as_view(), name='habitacion-detail'),
]