from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CarModelSerializer
from listings.models import CarModel

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    '''
    Returns a list of routes, each represented by a dictionary with an HTTP
    method as the key and a URL path as the value
    '''
    routes = [
        {'GET': '/api/project/id'}
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCarModel(request, pk):
    '''
    Gets car models based on car makes and returns
    a JSON representation of the serialized data
    '''
    car_model = CarModel.objects.filter(car_make=pk)
    serializer = CarModelSerializer(car_model, many=True)
    return Response(serializer.data)
