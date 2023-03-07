from django.contrib import admin
from django.urls import path
from .views import registerFacultyView
urlpatterns = [
    path('registerFaculty',view=registerFacultyView.as_view()),
]
