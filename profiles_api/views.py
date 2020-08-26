#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiviews = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to traditional django view',
            'Gives you the more control over applcation logic',
            'Is manually mapped to urls',
        ]

        return Response({'message': 'Hello','an_apiviews': an_apiviews})
