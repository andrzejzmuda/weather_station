from django.db.models import Subquery, OuterRef
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (Cities, GeoData, WeatherCodes,CurrentWeather,
                    Minutely15Weather, HourlyWeather, DailyWeather)

from .serializers import (CitiesSerializer, WeatherCodesSerializer,GeoDataSerializer,
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


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [permissions.IsAuthenticated]


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

    def get_queryset(self):
        latest = CurrentWeather.objects.filter(
            geo_id=OuterRef("geo_id")
        ).order_by("-weather_timestamp")

        qs = CurrentWeather.objects.filter(
            id=Subquery(latest.values("id")[:1])
        )
        qs = qs.annotate(
            geo_city=Subquery(
                Cities.objects.filter(id=OuterRef("geo_id")).values("name")[:1]
            )
        )
        qs = qs.annotate(
            weather_description=Subquery(
                WeatherCodes.objects.filter(code=OuterRef("weather_code")).values("description")[:1]
            )
        )
        return qs

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
