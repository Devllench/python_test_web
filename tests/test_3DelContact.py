from model.class_test_contact import Auth
import time
time.sleep(5)


def test_delete_contact(app):
    # логинемся
    app.session.login_site(Auth(username="admin", password="secret"))
    # добавляем контакт
    time.sleep(10)
    app.contact.delete_first_contact()
    app.session.logout_site()