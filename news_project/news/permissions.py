from rest_framework.permissions import BasePermission


class IsReader(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "reader"


class IsJournalist(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "journalist"


class IsEditor(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "editor"