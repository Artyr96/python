from model.new_user import New_user


def test_modify_user_name(app):
    app.session.login(username="artur", password="artur")
    app.newuser.modify(New_user(name="te3", password="321"))
    app.session.logout()
