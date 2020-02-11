def test_delet_first_group(app):
    app.session.login_site(Auth(username="admin", password="secret"))
    app.group.delet_first_group()
    app.session.logout_site()