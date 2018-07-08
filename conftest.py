import pytest
from fixture.application import App
import json
import jsonpickle
import os.path
import importlib
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        conf_file_full_path =os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(conf_file_full_path) as config_file:
            target = json.load(config_file)
    return target

@pytest.fixture
def appl(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = App(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(login=web_config["login"], password=web_config["password"])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(_host=db_config["host"], _database=db_config["database"], _user=db_config["user"], _password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session")
def orm(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(_host=db_config["host"], _database=db_config["database"], _user=db_config["user"], _password=db_config["password"])
    #def fin():
     #   ormfixture.destroy()
    #request.addfinalizer(fin)
    return ormfixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).test_data   #data means python package here
                                                                   # test_data - data, discribed in test_data in groups.py

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

