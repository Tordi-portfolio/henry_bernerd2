from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin', views.admin, name='admin'),
    path('payments', views.payments, name='payments'),
]