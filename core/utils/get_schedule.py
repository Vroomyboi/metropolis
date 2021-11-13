import datetime
from django.utils import timezone


def get_week_schedule_json(user):
    if user.is_authenticated:
        date = timezone.localdate()

        result = {}

        for day in range(7):
            result[date.isoformat()] = user.schedule(target_date=date)
            date += datetime.timedelta(days=1)
        return result
    else:
        return '{}'
