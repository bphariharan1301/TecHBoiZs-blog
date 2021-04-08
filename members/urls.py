from os import name
from django.urls import path
from .views import *
from . import views

# from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserUpdateView.as_view(), name='edit_profile'),
    path('password/', PasswordsUpdateView.as_view(), name='change-password'),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create_profile_page'),
    # path('login/', UserLoginView.as_view(), name="login")
    # path('login/', UserLoginView.as_view(), name='login'),
]