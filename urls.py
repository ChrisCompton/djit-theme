from django.urls import path, include

from . import views

app_name = 'djit_theme'

urlpatterns = [
    path('', views.view_default_theme, name='view_default_theme'),
]
