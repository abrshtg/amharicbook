from django.test import SimpleTestCase
from django.urls import resolve, reverse
from .views import HomePageView

class HomePageTest(SimpleTestCase):
    def setUP(self):
        url = reverse('home')
        return self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.setUP().status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.setUP(), "home.html")

    def test_homepage_contain_correct_html(self):
        self.assertContains(self.setUP(), 'home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.setUP(), 'I should not be in the html!')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)