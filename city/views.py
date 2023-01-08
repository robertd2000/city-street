from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer, CityStreetsSerializer
from .models import City


class Cities(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityStreets(generics.GenericAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get(self, request, pk):
        streets = City.objects.get(pk=pk)
        streets = CityStreetsSerializer(streets)
        return Response(streets.data)
