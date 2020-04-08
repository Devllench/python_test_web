# -*- coding: utf-8 -*-
from model.class_test_contact import Contactdate

import time


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
    # добавляем контакт
    app.contact.create(Сontact_test1)
