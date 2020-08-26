#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiviews = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to traditional django view',
            'Gives you the more control over applcation logic',
            'Is manually mapped to urls',
        ]

        return Response({'message': 'Hello','an_apiviews': an_apiviews})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling full update of an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handles partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'DELETE'})
