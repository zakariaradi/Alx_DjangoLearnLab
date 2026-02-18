from django.urls import path
from .views import followuser, unfollowuser

urlpatterns += [
    path('follow/<int:user_id>/', followuser),
    path('unfollow/<int:user_id>/', unfollowuser),
]

