# -*- coding: utf-8 -*-
import pytest
from model.сlass_test_group import Group, Auth
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.create_group(Group(group_name="tested", group_header="test head rec", group_footer="test foot rec"))
    app.session.logout_site()


def test_add_empty_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.create_group(Group(group_name="", group_header="", group_footer=""))
    app.session.logout_site()
