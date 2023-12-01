from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser

class HigherAuthoritiesPremission(permissions.BasePermission):

    def has_permission(self, request, view):
        if(isinstance(request.user,AnonymousUser)):
            return False
        if(request.user.role == 'Owner' or request.user.role == 'Admin'):
            return True
        else:
            return request.user.groups.filter(name="Higher Authorities").exists()
        
class MaintenanceManagementPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if(isinstance(request.user,AnonymousUser)):
            return False
        if(request.method == 'GET' or request.user.role == 'Admin'):
            return True
        elif(request.method == 'POST' and request.user.groups.filter(name='Higher Authorities')):
            return True
        elif(request.method == 'PATCH' and request.user.groups.filter(name='Higher Authorities')):
            if('status' in request.data):
                if(request.data['status'] == 'Verified' or request.data['status'] == 'Unverified'):
                    return True
            return False
        else:
            return request.user.groups.filter(name='Maintenance Manager').exists()
        