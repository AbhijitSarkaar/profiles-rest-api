from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Use http methods as functions',
            'it is similar to traditional views. only used for building apis'
        ]

        return Response({
            'message': 'Hello',
            'api_view': an_apiview
        })

    def post(self, request):
        """Create a hello message with name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response( 
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )
    
    
    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({
            'method': 'PUT'
        })


    def patch(self, request, pk=None):
        """Handle partial updating an object"""

        return Response({
            'method': 'PATCH'
        })


    def delete(self, request, pk=None):
        """Handle deleting an object"""

        return Response({
            'method': 'DELETE'
        })


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'uses actions, lists, create, retrive, update, partial_update',
            'automatically maps to urls using Routers',
            'provides more functionality with less code'
        ]
        
        return Response({
            'message': 'hello', 'a_viewset': a_viewset
        })
    
    def create(self, request):
        """Creates a new object"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            return Response({
                'message': f'Hello {name}' 
            })
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by ID"""

        return Response({
            'http_message': 'GET'
        })
    
    def update(self, request, pk=None):
        """Handle update an object by ID"""

        return Response({
            'http_message': 'PUT'
        })
    
    def partial_update(self, request, pk=None):
        """Handle partial update an object by ID"""

        return Response({
            'http_message': 'PATCH'
        })

    def destroy(self, request, pk=None):
        """Handle Remove an object by ID"""

        return Response({
            'http_message': 'DELETE'
        })


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating an updating profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields= ('name', 'email', )







