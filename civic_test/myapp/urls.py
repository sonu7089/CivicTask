from django.urls import path
from .views import run_pipeline

urlpatterns = [
    path('run_pipeline/', run_pipeline, name = 'run_pipeline'),
]