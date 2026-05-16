from django.apps import AppConfig

from apscheduler.schedulers.background import BackgroundScheduler


class ForecastConfig(AppConfig):
    name = 'forecast'
    scheduler_started = False

    def ready(self):
        if not self.scheduler_started:
            from forecast.scheduler.get_forecast import (
                get_current, get_daily, get_hourly, get_minutely_15)
            scheduler = BackgroundScheduler()
            scheduler.add_job(get_current, 'interval', minutes=15)
            scheduler.add_job(get_minutely_15, 'interval', hours=1)
            scheduler.add_job(get_hourly, 'interval', hours=4)
            scheduler.add_job(get_daily, 'interval', hours=8)
            scheduler.start()
            self.scheduler_started = True
