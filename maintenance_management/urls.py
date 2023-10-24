
from django.urls import path,include
from .router import maintenanceIssueRouter
from .views import MaintenanceIssueStatusAndCountView
urlpatterns = [
    path('maintenanceStatusAndCount/',view=MaintenanceIssueStatusAndCountView.as_view()),
    path("",include(maintenanceIssueRouter.urls)),
]
