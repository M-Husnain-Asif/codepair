from django.urls import path
from . import views

urlpatterns = [
    path('',views.problems_set),
    path('add/',views.add_problem)

]