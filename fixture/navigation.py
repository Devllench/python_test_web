# в разработке
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/adressbook/group.php")

    def open_group_page(self):
        wd = self.wd
        # open group page
        wd.find_element_by_link_text("groups").click()