from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

from .models import Library, Book
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render



# =====================================================
# Books Views
# =====================================================

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# =====================================================
# Authentication
# =====================================================

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


# =====================================================
# Role-Based Access Control (Task 3)
# =====================================================

@user_passes_test(lambda user: user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(lambda user: user.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(lambda user: user.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# =====================================================
# Custom Permissions (Task 4)
# =====================================================

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return HttpResponse("Add Book - Permission Granted")


@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    return HttpResponse("Edit Book - Permission Granted")


@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    return HttpResponse("Delete Book - Permission Granted")


@user_passes_test(lambda user: user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(lambda user: user.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(lambda user: user.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')






