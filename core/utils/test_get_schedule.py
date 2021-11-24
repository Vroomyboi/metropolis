from django.contrib.auth.models import AnonymousUser
from django.test import TestCase

from ..models import Event, Organization, Term, Timetable, User
from .get_schedule import *


def create_current_term():
    now = timezone.now()
    term = Term(start_date=now, end_date=now +
                datetime.timedelta(days=100), timetable_format='week')
    term.save()
    return term


def create_timetable(user, term):
    timetable = Timetable(term=term, owner=user)
    timetable.save()


def create_user() -> User:
    user = User(username="bob")
    user.save()
    return user


def create_school_org(user: User) -> Organization:
    school_org = Organization(owner=user)
    school_org.save()
    return school_org


def create_winter_break(school_org: Organization, term: Term):
    now = timezone.now()
    event = Event(start_date=now, end_date=now +
                  datetime.timedelta(days=10), organization=school_org, term=term, is_instructional=False)
    event.save()


class GetWeekScheduleInfoTests(TestCase):
    def test_no_current_term_logged_in(self):
        user = create_user()
        info = get_week_schedule_info(user)
        self.assertFalse(info.nudge_add_timetable)
        self.assertTrue(info.logged_in)

    def test_no_current_term_not_logged_in(self):
        user = AnonymousUser()
        info = get_week_schedule_info(user)
        self.assertFalse(info.nudge_add_timetable)
        self.assertFalse(info.logged_in)

    def test_current_term_logged_in_not_personalized(self):
        create_current_term()
        user = create_user()
        info = get_week_schedule_info(user)
        self.assertTrue(info.nudge_add_timetable)
        self.assertTrue(info.logged_in)

    def test_current_term_personalized(self):
        create_current_term()
        user = create_user()
        create_timetable(user, Term.get_current())
        info = get_week_schedule_info(user)
        self.assertFalse(info.nudge_add_timetable)
        self.assertTrue(info.logged_in)

    def test_winter_break_personalized(self):
        term = create_current_term()
        user = create_user()
        school_org = create_school_org(user)
        create_winter_break(school_org, term)
        create_timetable(user, term)
        info = get_week_schedule_info(user)
        self.assertFalse(info.nudge_add_timetable)
        self.assertTrue(info.logged_in)


class GetScheduleNudgeMessageTests(TestCase):
    def test_current_term_logged_in_personalized(self):
        create_current_term()
        info = WeekScheduleInfo(
            json_data="{}", logged_in=True, nudge_add_timetable=False)
        self.assertEqual(
            get_schedule_nudge_message(info), "")

    def test_current_term_logged_in_not_personalized(self):
        create_current_term()
        info = WeekScheduleInfo(
            json_data="{}", logged_in=True, nudge_add_timetable=True)
        self.assertTrue(
            "Add your timetable" in get_schedule_nudge_message(info))

    def test_current_term_not_logged_in(self):
        create_current_term()
        info = WeekScheduleInfo(
            json_data="{}", logged_in=False, nudge_add_timetable=True)
        self.assertTrue("Sign up" in get_schedule_nudge_message(info))
