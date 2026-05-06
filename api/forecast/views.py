from .models import (WeatherCodes, GeoData, CurrentWeather,
                    Minutely15Weather, HourlyWeather, DailyWeather)
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .serializers import (WeatherCodesSerializer,GeoDataSerializer,
                          CurrentWeatherSerializer, Minutely15WeatherSerializer,
                          HourlyWeatherSerializer, DailyWeatherSerializer)


class WeatherCodesViewSet(viewsets.ModelViewSet):
    queryset = WeatherCodes.objects.all()
    serializer_class = WeatherCodesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GeoDataViewSet(viewsets.ModelViewSet):
    queryset = GeoData.objects.all()
    serializer_class = GeoDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CurrentWeatherViewSet(viewsets.ModelViewSet):
    queryset = CurrentWeather.objects.all()
    serializer_class = CurrentWeatherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Minutely15WeatherViewSet(viewsets.ModelViewSet):
    queryset = Minutely15Weather.objects.all()
    serializer_class = Minutely15WeatherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HourlyWeatherViewSet(viewsets.ModelViewSet):
    queryset = HourlyWeather.objects.all()
    serializer_class = HourlyWeatherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DailyWeatherViewSet(viewsets.ModelViewSet):
    queryset = DailyWeather.objects.all()
    serializer_class = DailyWeatherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
