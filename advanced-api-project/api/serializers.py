from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model data.
    Includes custom validation to ensure the publication year
    is not set in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Prevents books from being published in a future year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model data.
    Includes a nested BookSerializer to dynamically serialize
    all books written by the author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
