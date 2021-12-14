from celery.schedules import crontab
from celery.task import periodic_task
from .models import User

@periodic_task(run_every=crontab(0, 0, day_of_month='1'))
def every_monday_morning():
    for user in User.objects.all().iterator():
        user.coins -= 5
        user.save()