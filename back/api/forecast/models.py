from django.db import models


class WeatherCodes(models.Model):
    code = models.FloatField(unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Code {self.code}: {self.description}"

    class Meta:
        verbose_name = "WeatherCode"
        verbose_name_plural = "WeatherCodes"
        app_label = "forecast"
        unique_together = ('code', 'description')


class Cities(models.Model):
    geo_id = models.ForeignKey('GeoData', on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} (Geo ID: {self.geo_id_id})"

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        app_label = "forecast"
        unique_together = ('geo_id', 'name')


class GeoData(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    elevation = models.FloatField(null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)
    timezone_abbreviation = models.CharField(max_length=30, null=True, blank=True)
    utc_offset_seconds = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude} ({self.timezone})"

    class Meta:
        verbose_name = "GeoData"
        verbose_name_plural = "GeoData"
        app_label = "forecast"
        unique_together = ('latitude', 'longitude')


class CurrentWeather(models.Model):
    geo_id = models.IntegerField(null=False, blank=False, default=1)
    weather_timestamp = models.DateTimeField(auto_now_add=True)
    temperature_2m = models.FloatField(null=True, blank=True)
    relative_humidity_2m = models.FloatField(null=True, blank=True)
    apparent_temperature = models.FloatField(null=True, blank=True)
    precipitation = models.FloatField(null=True, blank=True)
    rain = models.FloatField(null=True, blank=True)
    showers = models.FloatField(null=True, blank=True)
    snowfall = models.FloatField(null=True, blank=True)
    wind_speed_10m = models.FloatField(null=True, blank=True)
    wind_direction_10m = models.FloatField(null=True, blank=True)
    wind_gusts_10m = models.FloatField(null=True, blank=True)
    surface_pressure = models.FloatField(null=True, blank=True)
    cloud_cover = models.FloatField(null=True, blank=True)
    weather_code = models.FloatField(null=True, blank=True)
    is_day = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Weather #{self.geo_id} - {self.weather_timestamp}"

    class Meta:
        verbose_name = "CurrentWeather"
        verbose_name_plural = "CurrentWeather"
        app_label = "forecast"


class Minutely15Weather(models.Model):
    geo_id = models.IntegerField(null=False, blank=False, default=1)
    date = models.DateTimeField(null=True, blank=True)
    temperature_2m = models.FloatField(null=True, blank=True)
    relative_humidity_2m = models.FloatField(null=True, blank=True)
    weather_code = models.FloatField(null=True, blank=True)
    wind_speed_10m = models.FloatField(null=True, blank=True)
    rain = models.FloatField(null=True, blank=True)
    snowfall = models.FloatField(null=True, blank=True)
    snowfall_height = models.FloatField(null=True, blank=True)
    sunshine_duration = models.FloatField(null=True, blank=True)
    visibility = models.FloatField(null=True, blank=True)
    showers = models.FloatField(null=True, blank=True)
    precipitation = models.FloatField(null=True, blank=True)
    wind_speed_10m = models.FloatField(null=True, blank=True)
    wind_direction_10m = models.FloatField(null=True, blank=True)
    wind_gusts_10m = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Minutely15 Weather #{self.geo_id} - {self.date}"

    class Meta:
        verbose_name = "Minutely15Weather"
        verbose_name_plural = "Minutely15Weather"
        app_label = "forecast"
        unique_together = ('geo_id', 'date')


class HourlyWeather(models.Model):
    geo_id = models.IntegerField(null=False, blank=False, default=1)
    date = models.DateTimeField()
    temperature_2m = models.FloatField(null=True, blank=True)
    relative_humidity_2m = models.FloatField(null=True, blank=True)
    weather_code = models.FloatField(null=True, blank=True)
    surface_pressure = models.FloatField(null=True, blank=True)
    visibility = models.FloatField(null=True, blank=True)
    snow_depth = models.FloatField(null=True, blank=True)
    snowfall = models.FloatField(null=True, blank=True)
    showers = models.FloatField(null=True, blank=True)
    rain = models.FloatField(null=True, blank=True)
    precipitation = models.FloatField(null=True, blank=True)
    precipitation_probability = models.FloatField(null=True, blank=True)
    apparent_temperature = models.FloatField(null=True, blank=True)
    wind_speed_10m = models.FloatField(null=True, blank=True)
    uv_index = models.FloatField(null=True, blank=True)
    uv_index_clear_sky = models.FloatField(null=True, blank=True)
    sunshine_duration = models.FloatField(null=True, blank=True)
    cloud_cover = models.FloatField(null=True, blank=True)
    cloud_cover_low = models.FloatField(null=True, blank=True)
    wind_direction_10m = models.FloatField(null=True, blank=True)
    freezing_level_height = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Hourly Weather #{self.geo_id} - {self.date}"

    class Meta:
        verbose_name = "HourlyWeather"
        verbose_name_plural = "HourlyWeather"
        app_label = "forecast"
        unique_together = ('geo_id', 'date')


class DailyWeather(models.Model):
    geo_id = models.IntegerField(null=False, blank=False, default=1)
    date = models.DateTimeField()
    weather_code = models.FloatField(null=True, blank=True)
    temperature_2m_max = models.FloatField(null=True, blank=True)
    temperature_2m_min = models.FloatField(null=True, blank=True)
    apparent_temperature_max = models.FloatField(null=True, blank=True)
    apparent_temperature_min = models.FloatField(null=True, blank=True)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    daylight_duration = models.FloatField(null=True, blank=True)
    sunshine_duration = models.FloatField(null=True, blank=True)
    wind_speed_10m_max = models.FloatField(null=True, blank=True)
    wind_gusts_10m_max = models.FloatField(null=True, blank=True)
    rain_sum = models.FloatField(null=True, blank=True)
    showers_sum = models.FloatField(null=True, blank=True)
    snowfall_sum = models.FloatField(null=True, blank=True)
    precipitation_sum = models.FloatField(null=True, blank=True)
    precipitation_hours = models.FloatField(null=True, blank=True)
    precipitation_probability_max = models.FloatField(null=True, blank=True)
    temperature_2m_mean = models.FloatField(null=True, blank=True)
    surface_pressure_mean = models.FloatField(null=True, blank=True)
    precipitation_probability_mean = models.FloatField(null=True, blank=True)
    cloud_cover_min = models.FloatField(null=True, blank=True)
    cloud_cover_max = models.FloatField(null=True, blank=True)
    cloud_cover_mean = models.FloatField(null=True, blank=True)
    visibility_max = models.FloatField(null=True, blank=True)
    visibility_min = models.FloatField(null=True, blank=True)
    visibility_mean = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Daily Weather #{self.geo_id} - {self.date}"

    class Meta:
        verbose_name = "DailyWeather"
        verbose_name_plural = "DailyWeather"
        app_label = "forecast"
        unique_together = ('geo_id', 'date')