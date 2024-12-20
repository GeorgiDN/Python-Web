from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.urls import reverse
from forumApp.posts.views import IndexView

UserModel = get_user_model()


class TestIndexViewIntegration(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "someUser",
            "email": "user@user.com",
            "password": "asdfihrw?@#$%^#deqwhqwe"
        }

    def test__get_template_names__authenticated_user__returns_auth_template(self):
        user = UserModel.objects.create_user(
            username="someUser",
            email="user@user.com",
            password="testpass123",
        )

        self.client.login(
            email="user@user.com",
            password="testpass123"
            )

        response = self.client.get(reverse("index"))

        self.assertEqual(response.template_name, ["common/index_logged_in.html"])


class TestIndexViewUnit(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "someUser",
            "email": "user@user.com",
            "password": "asdfihrw?@#$%^#deqwhqwe"
        }

        self.factory = RequestFactory()

    def test__get_template_names__authenticated_user__returns_auth_template(self):
        request = self.factory.get(reverse("index"))
        request.user = UserModel.objects.create_user(**self.credentials)
        response = IndexView.as_view()(request)
        self.assertEqual(response.template_name, ["common/index_logged_in.html"])

    def test__get_template_names__not_authenticated_user__returns_index_no_user_template(self):
        request = self.factory.get(reverse("index"))
        request.user = AnonymousUser()

        response = IndexView.as_view()(request)

        self.assertEqual(response.template_name,  ["common/index.html"])
