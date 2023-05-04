from rest_framework import permissions


class HigherAuthoritiesPremission(permissions.BasePermission):

    def has_permission(self, request, view):
        if(request.user.role == 'Owner'):
            return True
        else:
            return request.user.groups.filter(name="Higher Authorities").exists()