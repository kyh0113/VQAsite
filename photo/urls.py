from django.urls import path
from .views import *
from . import views

app_name='photo'

urlpatterns = [
    path('upload/', PhotoUploadView.as_view() , name="photo_upload"), 
    path('photo/', views.photo_view, name="photo_view"),
    path('photo/<int:pk>/', views.photo_detail, name="photo_detail"),
]
