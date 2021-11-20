import datetime
from dataclasses import dataclass
import json
import rest_framework.utils.encoders
from django.utils import timezone

from .. import models


@dataclass
class DaySchedule:
    schedule: dict
    is_personal: bool


class JSONEncoder(rest_framework.utils.encoders.JSONEncoder):
    """
    Extends rest_framework JSONEncoder to encode DaySchedule.
    """

    def default(self, obj):
        if isinstance(obj, DaySchedule):
            return obj.__dict__
        return super().default(obj)


def generic_day_schedule(term, date) -> DaySchedule:
    schedule = term.day_schedule(target_date=date) if term is not None else []
    return DaySchedule(schedule, False)


def get_week_schedule(user) -> dict:
    date = timezone.localdate()

    if user.is_authenticated:
        result = {}  # TODO: use a dictionary comprehension

        for day in range(7):
            term = models.Term.get_current(target_date=date)
            # first try using personal day schedule
            day_schedule = DaySchedule(user.schedule(target_date=date), True)
            # switch to generic day schedule if personal day schedule is empty
            if len(day_schedule.schedule) == 0:
                day_schedule = generic_day_schedule(term, date)
            result[date.isoformat()] = day_schedule
            date += datetime.timedelta(days=1)

        return result
    else:
        result = {}  # TODO: use a dictionary comprehension

        for day in range(7):
            term = models.Term.get_current(target_date=date)
            result[date.isoformat()] = generic_day_schedule(term, date)
            date += datetime.timedelta(days=1)
        return result


def get_week_schedule_json(user) -> str:
    return json.dumps(get_week_schedule(user), cls=JSONEncoder)
