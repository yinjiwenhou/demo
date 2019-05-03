from rest_framework.permissions import BasePermission

from .models import UserModel

class SelfReadPremisssion(BasePermission):

    def has_permission(self, request, view):
        return int(request.user.id) == int(view.kwargs["id"])
