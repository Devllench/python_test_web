# ttaset
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def update(self, group):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.input_group_date(group)
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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)