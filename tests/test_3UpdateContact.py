# -*- coding: utf-8 -*-
from model.class_test_contact import Auth, Contactdate


def test_update_contact(app):
    # Данные используемые для тестирования
    Сontact_test1 = Contactdate(firstname="testnameupdate", middlename="testname3up", lastname="testname3up",
                                nickname="testniki-up", title="testtitle-up", company="testcompany-up",
                                address="test adress 12-up",
                                home="testhome-up", mobile="testmob-up", work="testwork-up", fax="testfax-up",
                                email="test-up@mail.ru",
                                email2="testmail4-up@mail.ru", email3="testmail3-up@mail.ru", homepage="testhomepage-up",
                                bday="1", bmonth="January", byear="2002", ayear="2012", amonth="May", aday="12",
                                address2="test adr-up", phone2="testhome-up", notes="test-up")
    # логинемся
    app.session.login_site(Auth(username="admin", password="secret"))
    # добавляем контакт
    app.contact.update(Сontact_test1)
    app.session.logout_site()