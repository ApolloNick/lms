import pytest
from django.core.management import call_command
from rest_framework.test import APIClient
from groups.models import Group
from teachers.models import Teacher


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture()
def group():
    group_object = Group.objects.create(name='Name', course='Course')
    return group_object


@pytest.fixture()
def position():
    position = Teacher.PositionLevel.TEACHER
    yield position


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', f'tests/fixtures/groups.json')
        call_command('loaddata', f'tests/fixtures/teachers.json')  # когда я запускаю тесты у меня каждый раз
        # прогружается вся база, так и должно быть?


@pytest.fixture(scope='function')
def client_api():
    client = APIClient()
    return client
