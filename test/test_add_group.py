# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="123123", header="123123", footer="123123"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
