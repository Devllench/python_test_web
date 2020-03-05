import pytest
from fixture.application import Application
from model.сlass_test_group import Auth

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login_site(Auth(username="admin", password="secret"))
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout_site()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
