def test_delete_user(app):
    app.session.login(username="artur", password="artur")
    app.newuser.delete_user()
    app.session.logout()