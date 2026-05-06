from django.contrib import admin

from .models import (WeatherCodes, GeoData, CurrentWeather,
                    Minutely15Weather, HourlyWeather, DailyWeather)

admin.site.register(WeatherCodes)
admin.site.register(GeoData)
admin.site.register(CurrentWeather)
admin.site.register(Minutely15Weather)
admin.site.register(HourlyWeather)
admin.site.register(DailyWeather)
