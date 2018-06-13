import pytest
from fixture.application import App

fixture = None


@pytest.fixture
def appl():
    global fixture
    if fixture is None:
        fixture = App()
    elif not fixture.is_valid():
        fixture = App()
    fixture.session.ensure_login('admin', 'secret')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture