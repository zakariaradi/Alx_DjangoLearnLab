from django.urls import path
from .views import RegisterView, LoginView, followuser, unfollowuser

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('follow/<int:user_id>/', followuser, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollowuser, name='unfollow-user'),
]
