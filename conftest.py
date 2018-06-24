import pytest
from fixture.application import App

fixture = None


@pytest.fixture
def appl(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = App(browser=browser, base_url=base_url)
    elif not fixture.is_valid():
        fixture = App(browser=browser, base_url=base_url)
    fixture.session.ensure_login('admin', 'secret')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://127.0.0.1/addressbook/")