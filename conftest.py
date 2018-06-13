import pytest
from fixture.application import App

fixture = None


@pytest.fixture
def appl():
    global fixture
    if fixture is None:
        fixture = App()
        fixture.session.login('admin', 'secret')
    elif not fixture.is_valid():
        fixture = App()
        fixture.session.login('admin', 'secret')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture