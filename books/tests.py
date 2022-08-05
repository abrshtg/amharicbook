from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book, Review


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Harry Potter", author="JK Rowling", price="25.00"
        )

        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123"
        )

        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="An excellent review!."
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.author, "JK Rowling")
        self.assertEqual(self.book.price, "25.00")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        non_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(non_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "An excellent review!.")
        self.assertTemplateUsed(response, "books/book_detail.html")
