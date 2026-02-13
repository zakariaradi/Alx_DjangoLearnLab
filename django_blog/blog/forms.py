from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


# =========================
# User Forms
# =========================

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


# =========================
# Post Form
# =========================

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


# =========================
# Comment Form (IMPORTANT)
# =========================

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) < 2:
            raise forms.ValidationError("Comment must contain at least 2 characters.")
        return content
