from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """  Test Api View """

    serializer_class = serializers.HelloSerializers

    def get(self, request, formate=None):
        """Return a list of An ApiView Features"""

        apiview = [
           'Uses HTTP method as function (get, post, put, patch & delete)',
           'Is similar to a traditional Django View',
           'Gives us the most control over our application logic',
           'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello APIView', 'apiview': apiview})

    def post(self, request):
        """Create a hello message with our Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            #message = f'Hello {name}'
            message = name
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an Object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle updating partially an Object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle Deleting an Object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test HelloViewSet API"""
    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a Hello Message"""
        viewset = [
             'Uses actions (list, create, retrieve, update, partial_update, destroy)',
             'Automatically maps to URLs using Routers',
             'Provides more functionality with less code'
        ]

        return Response({'message': 'ViewSet Main Features', 'viewset': viewset})

    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': name})
        else:
           return Response(
               serializer.errors,
               status=status.HTTP_400_BAD_REQUEST
           )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial_updating an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle destroying an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating & updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.userProfileManager.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle Creating User Authentication Tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
