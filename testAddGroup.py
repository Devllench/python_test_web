# -*- coding: utf-8 -*-
import pytest
from сlass_test_group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="tested", group_header="test head rec", group_footer="test foot rec"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="", group_header="", group_footer=""))
    app.logout()

