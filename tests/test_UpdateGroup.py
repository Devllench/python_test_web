# -*- coding: utf-8 -*-
from model.сlass_test_group import Group, Auth


def test_update_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.update(Group(group_name="tested3up", group_header="test head rec3up", group_footer="test foot rec3up"))
    app.open_home_page()
    app.session.logout_site()
