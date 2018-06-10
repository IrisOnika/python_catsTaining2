import pytest
from fixture.application import App


@pytest.fixture(scope='session')
def appl(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture