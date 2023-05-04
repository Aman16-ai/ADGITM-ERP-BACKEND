from django.contrib import admin
from django.urls import path
from .views import registerFacultyView,userView,LoginView
urlpatterns = [
    path('registerFaculty',view=registerFacultyView.as_view()),
    path("user",view=userView.as_view()),
    path("login/",view=LoginView.as_view())
]
