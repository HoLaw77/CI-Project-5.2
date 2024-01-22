from django.urls import path
from . import views
from .views import show_profile

urlpatterns = [
    path('customer', views.show_profile, name='customer'),
    path('test', views.test, name='test'),
]