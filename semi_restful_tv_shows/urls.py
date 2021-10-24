from django.urls import path, include
from tv_shows_app import views

urlpatterns = [
    path('', views.index),
    path('shows/', include('tv_shows_app.urls')),
]
