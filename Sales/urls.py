from django.urls import path
from . import views

urlpatterns = [
    # add at least one dummy route so it imports
    path('', views.index, name='sales-index'),
]