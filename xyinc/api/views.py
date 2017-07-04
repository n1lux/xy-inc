from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from xyinc.api.models import Poi
from xyinc.api.serializers import PoiSerializer


# Create your views here.

@api_view(['GET'])
def index(request):
    return Response()


class PoisList(APIView):
    """
    List all Poi's or create a new poi
    """

    def get(self, request, format=None):
        pois = Poi.get()
        serializer = PoiSerializer(data=pois, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PoiSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchPoi(APIView):
    def get(self, request, format=None):
        param_x = request.query_params.get('x', None)
        param_y = request.query_params.get('y', None)
        d_max = request.query_params.get('d-max', None)

        if param_x is not None and param_y is not None and d_max is not None:
            results = Poi.search(x=param_x, y=param_y, radius=d_max)
        else:
            return Response({'message': "Need query params. ex: ?x=20&y=10&d-max=10"})

        serializer = PoiSerializer(data=results, many=True)
        serializer.is_valid()
        return Response(serializer.data)


