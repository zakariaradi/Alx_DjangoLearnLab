from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post, Comment, Tag


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
# Post Form (With Tags)
# =========================

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        tags_input = self.cleaned_data.get('tags')

        if tags_input:
            tag_names = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

            # Clear existing tags (important for update)
            instance.tags.clear()

            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        return instance


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
