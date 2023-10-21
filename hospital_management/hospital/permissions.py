# hospital/permissions.py

from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        return request.user and request.user.is_staff


class IsAdminForNonGet(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin for non-GET methods
        if request.method != 'GET':
            return request.user and request.user.is_staff
        return True  # Allow GET requests for all users
