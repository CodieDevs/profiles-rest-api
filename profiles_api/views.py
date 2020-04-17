from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """  Test Api View """

    def get(self, request, formate=None):
        """Return a list of An ApiView Features"""

        apiview = [
           'Uses HTTP method as function (get, post, put, patch & delete)',
           'Is similar to a traditional Django View',
           'Gives us the most control over our application logic',
           'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello APIView', 'apiview': apiview})
