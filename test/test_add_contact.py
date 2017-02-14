# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="first", middle_name="middle", last_name="last", nickname="fml", title="title"
                               , company_name="company", address1="addr", email="first.lastmiddle.@company.com",
                               birth_year="1980", address2="addr2"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", middle_name="", last_name="", nickname="", title="", company_name="",
                               address1="",
                               email="", birth_year="", address2=""))
    app.session.logout()
