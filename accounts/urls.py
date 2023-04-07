from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.base_response, name='first_test'),
]
