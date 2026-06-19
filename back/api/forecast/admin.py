from django.contrib import admin

from .models import (WeatherCodes, GeoData, Cities, CurrentWeather,
                    Minutely15Weather, HourlyWeather, DailyWeather)

admin.site.register(WeatherCodes)
admin.site.register(GeoData)
admin.site.register(Cities)


@admin.register(CurrentWeather)
class CurrentWeatherAdmin(admin.ModelAdmin):
    list_display = ('geo_id', 'temperature_2m', 'relative_humidity_2m')
    search_fields = ('geo_id',)


@admin.register(Minutely15Weather)
class Minutely15WeatherAdmin(admin.ModelAdmin):
    list_display = ('geo_id', 'date', 'precipitation')
    search_fields = ('geo_id',)


@admin.register(HourlyWeather)
class HourlyWeatherAdmin(admin.ModelAdmin):
    list_display = ('geo_id', 'date', 'temperature_2m', 'relative_humidity_2m')
    search_fields = ('geo_id',)

@admin.register(DailyWeather)
class DailyWeatherAdmin(admin.ModelAdmin):
    list_display = ('geo_id', 'date', 'temperature_2m_mean')
    search_fields = ('geo_id',)
