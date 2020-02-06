from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/adressbook/group.php")

    def open_group_page(self):
        wd = self.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # inin group  creation
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        # submit group creationnn
        wd.find_element_by_name("submit").click()

    def destroy(self):
        self.wd.quit()

    def input_data_contact(self, Contactdate):
        wd = self.wd
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
        # нажимаем кнопку home page
        wd.find_element_by_link_text("home page").click()
