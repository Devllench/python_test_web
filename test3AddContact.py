# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from class_test_contact import Auth, Сontact_test1


def is_alert_present(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        # открываем сайт
        wd.get("http://localhost/adressbook/index.php")
        # логинемся
        self.login_site(wd, Auth(username="admin", password="secret"))
        # добавляем контакт
        self.input_data_contact(wd, Сontact_test1)
        # добавляем фото (не работает)
        # self.test_add_img(wd)
        # нажимаем кнопку home page
        wd.find_element_by_link_text("home page").click()
        # разлагиниваемся
        wd.find_element_by_link_text("Logout").click()

    # def test_add_img(self,wd):
    #   wd.find_element_by_name("photo").click()
    #   wd.find_element_by_name("photo").clear()
    #   wd.find_element_by_name("photo").send_keys("C:\\fakepath\\1649022.jpg")

    def input_data_contact(self, wd, Contactdate):
        # press add new
        wd.find_element_by_link_text("add new").click()
        # input date
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contactdate.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contactdate.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contactdate.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contactdate.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contactdate.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contactdate.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contactdate.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        #wd.find_element_by_name("home").send_keys("t")
        #wd.find_element_by_name("home").send_keys(Keys.DOWN)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contactdate.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contactdate.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contactdate.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contactdate.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contactdate.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contactdate.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contactdate.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contactdate.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Contactdate.bday)
        wd.find_element_by_xpath("//div[@id='content']/form/select/option[3]").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Contactdate.bmonth)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[35]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contactdate.byear)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Contactdate.ayear)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Contactdate.amonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[4]").click()
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Contactdate.aday)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[12]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contactdate.address2)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contactdate.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contactdate.notes)
        # press enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login_site(self, wd, Auth):
        # логин
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(Auth.username)
        # пароль
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        # вводим пароль
        wd.find_element_by_name("pass").send_keys(Auth.password)
        # нажимаем кнопку логин
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
