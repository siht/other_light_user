from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    UserCreationSerializer,
    UserEditionSerializer,
    UserEditPasswordSerializer,
)
from .models import User
__all__ = ('UserViewSet',)


class UserViewSet(viewsets.ModelViewSet):
    '''
    User resource

    retrieve:
    get user by id

    list:
    return a list of users

    create:
    create a new user with hashed password

    update:
    update user information except password

    partial_update:
    update user information except password

    destroy:
    eliminate user by id
    '''
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return UserEditionSerializer
        elif self.action == 'set_password':
            return UserEditPasswordSerializer
        return UserCreationSerializer

    @action(detail=True, methods=['patch', 'put'])
    def set_password(self, request, pk=None):
        '''
        change the user password
        '''
        user = User.objects.get(pk=pk)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status': 'password set'})
