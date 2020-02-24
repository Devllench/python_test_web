# -*- coding: utf-8 -*-
from model.сlass_test_group import Group, Auth


def test_update_group(app):
    app.group.update(Group(group_name="tested3up", group_header="test head rec3up", group_footer="test foot rec3up"))
    app.open_home_page()


def test_update_group_name(app):
    app.group.update(Group(group_name="New testedname"))
    app.open_home_page()


def test_update_group_header(app):
    app.group.update(Group(group_header="New testedheader"))
    app.open_home_page()
