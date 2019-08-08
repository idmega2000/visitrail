from api.models.company import Company
from api.serializers import CompanyUserSerializer, UpdateUserSerializer, CompanyUserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class CompanyViewSet(viewsets.ModelViewSet):
    """Viewset to handle Company details"""

    http_method_names = ['post']
    queryset = Company.objects.all()

    def create(self, request):
        """Handles the creation of a new company
        Args:
            request(dict): the request data
        Return:
            dict: return the company
        """
        data = request.data
        # data['added_by'] = request.user
        print(request.user)
        serializer = CompanyUserSerializer(data=request.data)
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
