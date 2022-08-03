from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

# from accounts.forms import CustomUserCreationForm
# from accounts.views import SignupPageView


class CustomUserTest(TestCase):
    def test_create_user(self):
        # get a model
        User = get_user_model()

        # creat a user.
        user = User.objects.create_user(
            email="ab@email.com", username="ab", password="test123"
        )

        # now test the created user is created properly.
        self.assertEqual(user.email, "ab@email.com")  # is email correct
        self.assertEqual(user.username, "ab")  # is username is correct
        self.assertTrue(user.is_active)  # is user active
        self.assertFalse(user.is_staff)  # is user not a staff
        self.assertFalse(user.is_superuser)  # is user not a superuser

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            email="admin@email.com", username="admin", password="test123"
        )

        self.assertEqual(admin_user.email, "admin@email.com")
        self.assertEqual(admin_user.username, "admin")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTest(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "sign up")
        self.assertNotContains(self.response, "this must be not in the template")

    def test_signup_form(self):  
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        # form = self.response.context.get("form")
        # self.assertIsInstance(form, CustomUserCreationForm)
        # self.assertContains(self.response, "csrfmiddlewaretoken")

    # def test_signup_view(self):  # new
    #     view = resolve("/accounts/signup/")
    #     self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
