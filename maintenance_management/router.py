from rest_framework.routers import SimpleRouter
from .views import MaintenanceIssueViewSet, MaintenanceTypeViewSet, MaintenanceIssueCommentViewSet
maintenanceTypeRouter = SimpleRouter()
maintenanceTypeRouter.register("",MaintenanceTypeViewSet)
maintenanceIssueRouter = SimpleRouter()
maintenanceIssueRouter.register("",MaintenanceIssueViewSet)
maintenanceIssueCommentRouter = SimpleRouter()
maintenanceIssueCommentRouter.register("",MaintenanceIssueCommentViewSet)
