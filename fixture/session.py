import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_site(self, Auth):
        wd = self.app.wd
        # открываем сайт
        time.sleep(10)
        wd.get("http://localhost/adressbook/index.php")
        #wd.get("http://brokesite.ru/index.php")
        # логин
        #time.sleep(5)
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

    def logout_site(self):
        wd = self.app.wd
        #wd.switch_to_alert().accept()
        # разлагиниваемся
        wd.find_element_by_partial_link_text('Logout').click()
        # wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']").click()
        # wd.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        # wd.find_element_by_xpath("//a[contains(@href, '#')]").click()
        wd.find_element_by_name("user")

    def ensure_logout_site(self):
        wd = self.app.wd

        if self.is_logged_in():
            self.logout_site()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_partial_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text == "(" + username + ")"

    def ensure_login_site(self, Auth):
        wd = self.app.wd
        #wd.switch_to_alert().accept()  # решает проблему с запросов языка при открытии браузера
        if self.is_logged_in():
            if self.is_logged_in_as(Auth.username):
                return
            else:
                self.logout_site()
        self.login_site(Auth)
