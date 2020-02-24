# -*- coding: utf-8 -*-
from model.сlass_test_group import Group, Auth


def test_update_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.update(Group(group_name="tested3up", group_header="test head rec3up", group_footer="test foot rec3up"))
    app.open_home_page()
    app.session.logout_site()


def test_update_group_name(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.update(Group(group_name="New testedname"))
    app.open_home_page()
    app.session.logout_site()


def test_update_group_header(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.update(Group(group_header="New testedheader"))
    app.open_home_page()
    app.session.logout_site()