from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        #self.wd = webdriver.Firefox()
        self.wd = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True

        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # open home page

        wd.get("http://localhost/adressbook/group.php")
        #wd.get("http://brokesite.ru/group.php")

    def destroy(self):
        self.wd.quit()
