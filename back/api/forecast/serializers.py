from .models import (Cities, WeatherCodes, GeoData, CurrentWeather,
                    Minutely15Weather, HourlyWeather, DailyWeather)
from rest_framework import serializers


class WeatherCodesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherCodes
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=WeatherCodes.objects.all(),
                fields=['code', 'description'],
                message="A WeatherCodes entry with this code already exists."
            )
        ]


class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Cities.objects.all(),
                fields=['geo_id', 'name'],
                message="A City with this name already exists."
            )
        ]


class GeoDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoData
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=GeoData.objects.all(),
                fields=['latitude', 'longitude'],
                message="A GeoData entry with this latitude and longitude already exists."
            )
        ]


class CurrentWeatherSerializer(serializers.HyperlinkedModelSerializer):
    geo_city = serializers.CharField(read_only=True)
    weather_description = serializers.CharField(read_only=True)
    class Meta:
        model = CurrentWeather
        fields = '__all__'


class Minutely15WeatherSerializer(serializers.ModelSerializer):
    geo_city = serializers.CharField(read_only=True)
    weather_description = serializers.CharField(read_only=True)
    class Meta:
        model = Minutely15Weather
        fields = '__all__'
        list_serializer_class = serializers.ListSerializer


class HourlyWeatherSerializer(serializers.HyperlinkedModelSerializer):
    geo_city = serializers.CharField(read_only=True)
    weather_description = serializers.CharField(read_only=True)
    class Meta:
        model = HourlyWeather
        fields = '__all__'
        list_serializer_class = serializers.ListSerializer


class DailyWeatherSerializer(serializers.HyperlinkedModelSerializer):
    geo_city = serializers.CharField(read_only=True)
    weather_description = serializers.CharField(read_only=True)
    class Meta:
        model = DailyWeather
        fields = '__all__'
        list_serializer_class = serializers.ListSerializer