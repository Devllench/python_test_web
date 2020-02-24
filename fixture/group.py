# ttaset
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def update(self, new_group_date):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.input_group_date(new_group_date)
        # submit group updating
        wd.find_element_by_name("update").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # inin group  creation
        wd.find_element_by_name("new").click()
        self.input_group_date(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # delete first group
        wd.find_element_by_name("delete").click()

    def input_group_date(self, group):
        wd = self.app.wd
        self.change_feild_value("group_name", group.group_name)
        self.change_feild_value("group_header", group.group_header)
        self.change_feild_value("group_footer", group.group_footer)

    def change_feild_value(self, feild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(feild_name).click()
            wd.find_element_by_name(feild_name).clear()
            wd.find_element_by_name(feild_name).send_keys(text)