from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('account_delete/<profile>', views.account_delete, name='account_delete'),
]