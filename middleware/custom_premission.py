from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser

class HigherAuthoritiesPremission(permissions.BasePermission):

    def has_permission(self, request, view):
        if(isinstance(request.user,AnonymousUser)):
            return False
        if(request.user.role == 'Owner'):
            return True
        else:
            return request.user.groups.filter(name="Higher Authorities").exists()
        
class MaintenanceManagementPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if(isinstance(request.user,AnonymousUser)):
            return False
        if(request.method == 'GET'):
            return True
        elif(request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE'):
            return request.user.role == 'MM'
        else:
            return request.user.groups.filter(name='Maintenance Manager').exists()