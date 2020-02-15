class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_site(self, Auth):
        wd = self.app.wd
        # открываем сайт
        wd.get("http://localhost/adressbook/index.php")
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

    def logout_site(self):
        wd = self.app.wd
        # разлагиниваемся
        wd.find_element_by_partial_link_text('Logout').click()
        # wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']").click()
        # wd.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        # wd.find_element_by_xpath("//a[contains(@href, '#')]").click()
        wd.find_element_by_name("user")
