from model.class_test_contact import Auth
import time
time.sleep(5)


def test_delete_contact(app):
    # логинемся
    # добавляем контакт
    app.contact.delete_first_contact()
