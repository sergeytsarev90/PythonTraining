from fixture.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
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


