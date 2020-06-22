# -*- coding: utf-8 -*-
from model.new_user import New_user
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_app_dynamics_job_2(app):
    app.session.login(username="artur", password="artur")
    app.newuser.add(New_user(name="te2", username="te2", password="321"))
    app.session.logout()

def test_app_dynamics_job_1(app):
    app.session.login(username="artur", password="artur")
    app.newuser.add(New_user(name="te1", username="te1", password="321"))
    app.session.logout()

