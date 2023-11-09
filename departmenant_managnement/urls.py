
from django.urls import path,include
from .router import departmentRouter
urlpatterns = [
    path("",include(departmentRouter.urls)),
]
