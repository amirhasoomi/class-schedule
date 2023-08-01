from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (RegisterView, LoginView, ProfileView,
                    ChangePasswordView, MyProfileView,
                    UsertypeView, MembersView,
                    AllUsersView)


urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('changepassword', ChangePasswordView.as_view()),
    path('profile', MyProfileView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
    path('members', MembersView.as_view()),
    path('allusers', AllUsersView.as_view()),
    path('user_type/<int:pk>', UsertypeView.as_view({'patch': 'update'})),
]
