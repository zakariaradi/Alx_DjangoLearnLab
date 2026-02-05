from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering,
    and permission enforcement.
    """

    def setUp(self):
        """
        Set up test data and authenticated user.
        This runs before every test.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.author = Author.objects.create(name="George Orwell")

        self.book1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author
        )

        self.book_list_url = "/api/books/"
        self.book_create_url = "/api/books/create/"
        self.book_update_url = f"/api/books/update/{self.book1.id}/"
        self.book_delete_url = f"/api/books/delete/{self.book1.id}/"

    # ---------------------------
    # READ (List & Detail)
    # ---------------------------

    def test_list_books(self):
        """
        Ensure unauthenticated users can list books.
        """
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ---------------------------
    # CREATE
    # ---------------------------

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a book.
        """
        self.client.login(username='testuser', password='testpassword')

        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        data = {
            "title": "Forbidden Book",
            "publication_year": 2020,
            "author": self.author.id
        }

        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------
    # UPDATE
    # ---------------------------

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.login(username='testuser', password='testpassword')

        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(self.book_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    # ---------------------------
    # DELETE
    # ---------------------------

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.login(username='testuser', password='testpassword')

        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------------------------
    # FILTERING, SEARCHING, ORDERING
    # ---------------------------

    def test_filter_books_by_year(self):
        """
        Ensure books can be filtered by publication_year.
        """
        response = self.client.get("/api/books/?publication_year=1949")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        """
        Ensure books can be searched by title.
        """
        response = self.client.get("/api/books/?search=Animal")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """
        Ensure books can be ordered by publication_year.
        """
        response = self.client.get("/api/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["title"],
            "Animal Farm"
        )
