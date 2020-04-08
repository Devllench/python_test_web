from model.сlass_test_group import Auth


def test_delete_first_group(app):
    app.group.delete_first_group()


