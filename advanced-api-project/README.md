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
