# -*- coding: utf-8 -*-
from model.сlass_test_group import Group, Auth


def test_add_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.create(Group(group_name="tested", group_header="test head rec", group_footer="test foot rec"))
    app.open_home_page()
    app.session.logout_site()


def test_add_empty_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    app.open_home_page()
    app.session.logout_site()
