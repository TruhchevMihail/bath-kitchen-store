from django.urls import path
from . import views

name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]