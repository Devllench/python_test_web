#Классы
class Auth:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Group:

    def __init__(self, group_name, group_header, group_footer):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer