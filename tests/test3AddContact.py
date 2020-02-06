# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.class_test_contact import Auth, Contactdate


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    # Данные используемые для тестирования
    Сontact_test1 = Contactdate(firstname="testname", middlename="testname1", lastname="testname2",
                                nickname="testniki", title="testtitle", company="testcompany",
                                address="test adress 12",
                                home="testhome", mobile="testmob", work="testwork", fax="testfax",
                                email="test@mail.ru",
                                email2="testmail2@mail.ru", email3="testmail3@mail.ru", homepage="testhomepage",
                                bday="1", bmonth="January", byear="2000", ayear="2010", amonth="March", aday="10",
                                address2="test adr", phone2="testhome", notes="test")
    # логинемся
    app.session.login_site(Auth(username="admin", password="secret"))
    # добавляем контакт
    app.input_data_contact(Сontact_test1)
    app.session.logout_site()
