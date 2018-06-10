import pytest
from fixture.application import App


@pytest.fixture()
def appl(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture