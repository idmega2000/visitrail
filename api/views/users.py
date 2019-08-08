
from api.models.user import User, CompanyUser, Company
from api.serializers import UserSerializer, UpdateUserSerializer, CompanyUserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_list_or_404, get_object_or_404

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

class CompanyUserView(viewsets.ModelViewSet):
    """Viewset to handle company users"""
    permission_classes = (IsAuthenticated,)
    queryset = CompanyUser.objects.all()


    def create(self, request):
        """Handles the creation of a new users
        Args:
            request(dict): the request data
        Return:
            dict: return the user
        """
 
        company_exist = Company.objects.filter(id=request.data['company']).first()
        if not company_exist:
            error = {
                'status': 'error',
                'message': 'invalid company'
            }
            return Response(error, status=status.HTTP_403_FORBIDDEN)
        print(company_exist.added_by_id)
        print(request.user.id)

        if company_exist.added_by_id != request.user.id:
            error = {
                'status': 'error',
                'message': 'you do not have permission'
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        print(company_exist)
        for user in request.data['users']:
            user['added_by'] = request.user.id
            user['company'] = request.data['company']

        serializer = CompanyUserSerializer(data=request.data['users'], many=True)
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

    # def create(self, request):
    #     print(request.data)


    # def retrieve(self, request, pk):
    #     pass


    # def list(self, request, pk):
    #     pass

    # def destroy(self, request, pk):
    #     pass
