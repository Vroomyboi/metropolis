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
    logged_in: bool

    def get_is_personal_js(self):
        return "true" if self.is_personal else "false"

    def get_logged_in_js(self):
        return "true" if self.logged_in else "false"


def generic_day_schedule(term,date):
    if term is None:
        return []
    else:
        return term.day_schedule(target_date=date)


def get_week_schedule(user) -> WeekSchedule:
    term = models.Term.get_current()
    date = timezone.localdate()

    if user.is_authenticated:
        result = {}  # TODO: use a dictionary comprehension

        is_personal=False
        for day in range(7):
            day_schedule=user.schedule(target_date=date)
            if len(day_schedule)==0:
                day_schedule=generic_day_schedule(term, date)
            else:
                is_personal=True
            result[date.isoformat()] = day_schedule
            date += datetime.timedelta(days=1)

        return WeekSchedule(json.dumps(result, cls=JSONEncoder), is_personal, True)
    else:
        result = {}  # TODO: use a dictionary comprehension

        for day in range(7):
            result[date.isoformat()] = generic_day_schedule(term,date)
            date += datetime.timedelta(days=1)
        return WeekSchedule(json.dumps(result, cls=JSONEncoder), False, False)
