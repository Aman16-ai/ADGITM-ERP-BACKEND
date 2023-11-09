
from django.urls import path,include
from .router import maintenanceIssueRouter,maintenanceTypeRouter,maintenanceIssueCommentRouter
from .views import MaintenanceIssueStatusAndCountView
urlpatterns = [
    path('maintenanceStatusAndCount/',view=MaintenanceIssueStatusAndCountView.as_view()),
    path('maintenanceType/',include(maintenanceTypeRouter.urls)),
    path("maintenanceIssueComment/",include(maintenanceIssueCommentRouter.urls)),
    path("",include(maintenanceIssueRouter.urls)),
]
