from website import views
from django.urls import path, include

urlpatterns = [
    path('', views.website, name='register'),
]
