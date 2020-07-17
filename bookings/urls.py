from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('done/', views.confirmed, name='confirmed'),
    path('adminaccount/', views.admin, name='admin'),
    path('seebookings/', views.seebookings, name='seebookings')
]
