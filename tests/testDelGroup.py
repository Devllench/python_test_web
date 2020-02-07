from model.сlass_test_group import Auth


def test_delete_first_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.delete_first_group()
    app.open_home_page()
    app.session.logout_site()
