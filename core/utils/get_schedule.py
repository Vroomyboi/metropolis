import datetime
from dataclasses import dataclass
import json
from rest_framework.utils.encoders import JSONEncoder
from django.utils import timezone

from .. import models


@dataclass
class WeekSchedule:
    data: str
    is_personal: bool


def get_week_schedule(user) -> WeekSchedule:
    if user.is_authenticated:
        date = timezone.localdate()

        result = {}  # TODO: use a dictionary comprehension

        for day in range(7):
            result[date.isoformat()] = user.schedule(target_date=date)
            date += datetime.timedelta(days=1)
        return WeekSchedule(json.dumps(result, cls=JSONEncoder), True)
    else:
        term = models.Term.get_current()

        date = timezone.localdate()

        result = {}  # TODO: use a dictionary comprehension

        for day in range(7):
            # TODO: move term is None logic into a separate loop
            result[date.isoformat()] = term.day_schedule(
                target_date=date) if term is not None else []
            date += datetime.timedelta(days=1)
        return WeekSchedule(json.dumps(result, cls=JSONEncoder), False)
