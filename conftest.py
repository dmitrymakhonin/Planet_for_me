import pytest
from fixture.application import Application
from fixture.android import Android

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def andr():
    fixture=Android()
    return fixture