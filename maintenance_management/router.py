from rest_framework.routers import SimpleRouter
from .views import MaintenanceIssueViewSet
maintenanceIssueRouter = SimpleRouter()
maintenanceIssueRouter.register("",MaintenanceIssueViewSet)
