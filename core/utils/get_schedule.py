import datetime
import json
from rest_framework.utils.encoders import JSONEncoder
from django.utils import timezone

from .. import models


def get_week_schedule_json(user):
    if user.is_authenticated:
        date = timezone.localdate()

        result = {}

        for day in range(7):
            result[date.isoformat()] = user.schedule(target_date=date)
            date += datetime.timedelta(days=1)
        return json.dumps(result, cls=JSONEncoder)
    else:
        term = models.Term.get_current()

        if term is None:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        date = timezone.localdate()

        result = {}

        for day in range(7):
            result[date.isoformat()] = term.day_schedule(target_date=date)
            date += datetime.timedelta(days=1)
        return json.dumps(result, cls=JSONEncoder)
