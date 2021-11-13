import datetime
from rest_framework.renderers import JSONRenderer
from django.utils import timezone


def get_week_schedule_json(user):
    if user.is_authenticated:
        date = timezone.localdate()

        result = {}

        for day in range(7):
            result[date.isoformat()] = user.schedule(target_date=date)
            date += datetime.timedelta(days=1)
        return bytes.decode(JSONRenderer().render(result))
    else:
        return '{}'
