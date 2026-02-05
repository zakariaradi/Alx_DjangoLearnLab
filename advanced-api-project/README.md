## Book API Views

This project uses Django REST Framework generic views to manage Book resources.

### Available Endpoints

- GET /api/books/  
  Retrieves all books (public access)

- GET /api/books/<id>/  
  Retrieves a single book by ID (public access)

- POST /api/books/create/  
  Creates a new book (authenticated users only)

- PUT/PATCH /api/books/<id>/update/  
  Updates an existing book (authenticated users only)

- DELETE /api/books/<id>/delete/  
  Deletes a book (authenticated users only)

### Permissions
- Read-only endpoints are publicly accessible.
- Create, update, and delete operations require authentication.

## Filtering, Searching, and Ordering

The Book list endpoint supports advanced query features using Django REST Framework.

### Filtering
Filter books by:
- title
- publication_year
- author

Example:
GET /api/books/?publication_year=2022

### Searching
Search across book title and author name.

Example:
GET /api/books/?search=django

### Ordering
Order results by:
- title
- publication_year

Example:
GET /api/books/?ordering=-publication_year

## Testing

This project uses Django REST Framework's APITestCase to validate API behavior.

### What is tested:
- CRUD operations for Book endpoints
- Authentication and permission enforcement
- Filtering by publication_year
- Searching by title
- Ordering by publication_year

### Running tests:
python manage.py test api
