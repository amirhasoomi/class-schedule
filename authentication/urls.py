from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (RegisterView, LoginView,
                    ChangePasswordView, ProfileView)


urlpatterns = [
    path('admin/', include([
        path('login', LoginView.as_view()),
        path('register', RegisterView.as_view()),
        path('refresh', TokenRefreshView.as_view()),
        path('changepassword', ChangePasswordView.as_view()),
        path('profile', ProfileView.as_view()),
    ])),
]
