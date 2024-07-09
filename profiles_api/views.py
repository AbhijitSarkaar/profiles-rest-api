from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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



