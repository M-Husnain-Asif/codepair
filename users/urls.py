from .views import  UserCreateAPIView
from django.urls import path
urlpatterns = [
    path('register/',UserCreateAPIView.as_view(),name = 'register-user'),

]