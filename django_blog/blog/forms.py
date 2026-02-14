from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget

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
# Post Form (With TagWidget)
# =========================

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
            'content': forms.Textarea(attrs={'rows': 5}),
        }


# =========================
# Comment Form
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

        if not content or len(content.strip()) < 2:
            raise forms.ValidationError(
                "Comment must contain at least 2 characters."
            )

        return content
