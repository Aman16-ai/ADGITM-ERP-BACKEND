from rest_framework.routers import SimpleRouter
from .views import DepartmentViewSet
departmentRouter = SimpleRouter()

departmentRouter.register("",DepartmentViewSet)