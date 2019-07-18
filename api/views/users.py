from django.db import models
from api.models.user import User
from api.serializers import UserSerializer, UpdateUserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """Viewset to handle User details"""
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    http_method_names = ['get', 'patch', 'head']

    def retrieve(self, request, pk):
        """Handles the retrieval of a users
        Args:
            request(dict): the request data
            pk(uuid):  the uuid of the user to be fetched
        Return:
            dict: return the user
        """
        if (str(request.user.id) != pk):
            data = {
                'error': 'unauthorized',
                'message': 'Attempted to alter another user\'s record(s)'
            }
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(queryset)
        data = {
            'status': 'success',
            'data': serializer.data
        }
        return Response(data)

    def list(self, request):
        """Handles the retrieval of all users
        Args:
            request(dict): the request data
        Return:
            dict: return all the user
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        data = {
            'status': 'success',
            'data': serializer.data
        }
        return Response(data)      

    def partial_update(self, request, pk):
        """Handles the update of a users
        Args:
            request(dict): the request data
            pk(uuid):  the uuid of the user to be updated
        Return:
            dict: return the user
        """
        if (str(request.user.id) != pk):
            error = {
                'error': 'unauthorized',
                'message': 'Attempted to alter another user\'s record(s)'
            }
            return Response(error, status=status.HTTP_403_FORBIDDEN)
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class SignUpView(viewsets.ModelViewSet):
    """Viewset to handle User Signup"""
    http_method_names = ['post']
    queryset = User.objects.all()

    def create(self, request):
        """Handles the creation of a new users
        Args:
            request(dict): the request data
        Return:
            dict: return the user
        """
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': 'success',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        error = {
            'status': 'error',
            'message': serializer.errors
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
