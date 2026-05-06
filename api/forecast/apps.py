from django.apps import AppConfig

from apscheduler.schedulers.background import BackgroundScheduler
from forecast.scheduler.get_forecast import (get_current, get_daily, get_geo,
                                            get_hourly, get_minutely_15)
# from forecast.scheduler.tasks.geo import get_geo


class ForecastConfig(AppConfig):
    name = 'forecast'
    scheduler_started = False

    def ready(self):
        if not self.scheduler_started:
            scheduler = BackgroundScheduler()
            # scheduler.add_job(get_geo, 'interval', hours=1)
            scheduler.add_job(get_current, 'interval', hours=1)
            scheduler.add_job(get_minutely_15, 'interval', minutes=15)
            scheduler.add_job(get_hourly, 'interval', hours=1)
            scheduler.add_job(get_daily, 'interval', days=1)
            scheduler.start()
            self.scheduler_started = True
