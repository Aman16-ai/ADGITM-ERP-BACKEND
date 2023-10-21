
from django.urls import path,include
from .router import maintenanceIssueRouter
urlpatterns = [
    path("",include(maintenanceIssueRouter.urls))
]
