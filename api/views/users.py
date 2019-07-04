from django.db import models
from api.models.user import User
from api.serializers import UserSerializer, UpdateUserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    http_method_names = ['get', 'patch', 'head']

    def retrieve(self, request, pk):
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
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        data = {
            'status': 'success',
            'data': serializer.data
        }
        return Response(data)      

    def partial_update(self, request, pk):
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
    http_method_names = ['post']
    queryset = User.objects.all()

    def create(self, request, pk=None):
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
