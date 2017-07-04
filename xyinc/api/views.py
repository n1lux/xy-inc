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

        kwargs = {'x': request.query_params.get('x', None),
                  'y': request.query_params.get('y', None),
                  'radius': request.query_params.get('d-max', None)
                  }

        has_errors = _check_params(**kwargs)
        if has_errors:
            return Response(has_errors)

        results = Poi.search(**kwargs)
        serializer = PoiSerializer(data=results, many=True)
        serializer.is_valid()
        return Response(serializer.data)


def _check_params(**kwargs):
    errors = []
    for k, v in kwargs.items():
        try:
            int(v)
        except TypeError:
            errors.append({k: "Can not be null.", "ex": "Need query params. ex: ?x=20&y=10&d-max=10"})
        except ValueError:
            errors.append({k: "A valid integer is required."})
    return errors
