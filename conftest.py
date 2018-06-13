import pytest
from fixture.application import App

login ='admin'
password ='secret'


@pytest.fixture(scope='session')
def appl(request):
    fixture = App()
    fixture.session.login(login, password)
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture