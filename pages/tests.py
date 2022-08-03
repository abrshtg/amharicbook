from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from .views import HomePageView, AboutPageView


class HomePageTest(SimpleTestCase):
    def setUP(self):
        url = reverse("home")
        self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.setUP().status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.setUP(), "home.html")

    def test_homepage_contain_correct_html(self):
        self.assertContains(self.setUP(), "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.setUP(), "I should not be in the html!")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTest(TestCase):
    def setUp(self):
        url = reverse("about")
        self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.setUp().status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.setUp(), "about.html")

    def test_aboutpage_contain_correct_words(self):
        self.assertContains(self.setUp(), "about page")

    def test_aboutpage_not_contain_incorrect_words(self):
        self.assertNotContains(self.setUp(), "this is not in about page")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
