from rest_framework.permissions import BasePermission

from .utils import client_ip


class IsCreator(BasePermission):
    message = 'Only creator of the url is able to view stats and delete url.'

    def has_permission(self, request, view):
        return client_ip(request) == view.get_object().creator_ip
