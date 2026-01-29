from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm

from .models import Book, Library


@login_required
@permission_required("relationship_app.can_view", raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


@login_required
def admin_view(request):
    return render(request, "relationship_app/admin.html")


@login_required
def librarian_view(request):
    return render(request, "relationship_app/librarian.html")


@login_required
def member_view(request):
    return render(request, "relationship_app/member.html")


@login_required
@permission_required("relationship_app.can_create", raise_exception=True)
def add_book(request):
    return render(request, "relationship_app/add_book.html")


@login_required
@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "relationship_app/edit_book.html", {"book": book})


@login_required
@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("list_books")
