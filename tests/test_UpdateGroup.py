# -*- coding: utf-8 -*-
from model.сlass_test_group import Group


def test_update_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="update tested3up", group_header="update test head rec3up", group_footer="update test foot rec3up"))
    app.group.update(Group(group_name="tested3up", group_header="test head rec3up", group_footer="test foot rec3up"))
    #app.open_home_page()


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="update tested3up"))
    app.group.update(Group(group_name="New testedname"))

    #app.open_home_page()


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_header="update tested3up"))
    app.group.update(Group(group_header="New testedheader"))
    #app.open_home_page()
