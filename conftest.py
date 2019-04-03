from fixture.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Application(browser = browser,base_url = base_url)
        fixture.open_home_page()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.open_home_page()
    fixture.session.ensure_login(user="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
