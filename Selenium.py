# -*- coding: utf-8 -*-
from new_user import New_user
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_app_dynamics_job_2(app):
    app.login(username="artur", password="artur")
    app.add_user( New_user(name="te2", username="te2", password="321"))
    app.logout()

def test_app_dynamics_job_1(app):
    app.login(username="artur", password="artur")
    app.add_user(New_user(name="te1", username="te1", password="321"))
    app.logout()

