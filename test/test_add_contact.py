# -*- coding: utf-8 -*-
import pytest
from test.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="first", middle_name="middle", last_name="last", nickname="fml", title="title", company_name="company", address1="addr",
                        email="first.lastmiddle.@company.com", birth_year="1980", address2="addr2"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", nickname="", title="", company_name="", address1="",
                        email="", birth_year="", address2=""))
    app.logout()

if __name__ == '__main__':
    unittest.main()
