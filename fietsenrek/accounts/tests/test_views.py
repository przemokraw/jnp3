from django.contrib.auth.models import User
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from djet import assertions
from djet import restframework
from djet import testcases
from rest_auth.registration.views import RegisterView
from rest_framework import status

from accounts.factories import UserFactory


class RegistrationViewTestCase(assertions.StatusCodeAssertionsMixin,
                               restframework.APIViewTestCase):
    view_class = RegisterView
    middleware_classes = [
        SessionMiddleware,
        (MessageMiddleware, testcases.MiddlewareType.PROCESS_REQUEST),
    ]

    def test_view_should_raise_error__on_get(self):
        request = self.factory.get()

        response = self.view(request)

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_user_should_register_successfully__when_all_data_is_correct(self):
        username = 'username'
        email = 'email@email.com'
        password = 'passpass1234'
        data = {
            'username': username,
            'email': email,
            'password1': password,
            'password2': password,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_201_CREATED
        assert 'key' in response.data
        assert User.objects.count() == 1
        assert User.objects.first().username == username
        assert User.objects.first().email == email
        assert User.objects.first().check_password(password)

    def test_view_should_raise_error__when_email_is_missing(self):
        username = 'username'
        password = 'passpass1234'
        data = {
            'username': username,
            'password1': password,
            'password2': password,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_view_should_raise_error__when_username_is_missing(self):
        email = 'email@email.com'
        password = 'passpass1234'
        data = {
            'email': email,
            'password1': password,
            'password2': password,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_view_should_raise_error__when_passwords_are_mismatched(self):
        username = 'username'
        email = 'email@email.com'
        password = 'passpass1234'
        data = {
            'username': username,
            'email': email,
            'password1': password,
            'password2': '{}42'.format(password),
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_view_should_raise_error__when_username_is_already_registered(self):
        username = 'username'
        email = 'email@email.com'
        password = 'passpass1234'
        UserFactory(username=username)
        data = {
            'username': username,
            'email': email,
            'password1': password,
            'password2': password,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_view_should_raise_error__when_email_is_already_registered(self):
        username = 'username'
        email = 'email@email.com'
        password = 'passpass1234'
        UserFactory(email=email)
        data = {
            'username': username,
            'email': email,
            'password1': password,
            'password2': password,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
