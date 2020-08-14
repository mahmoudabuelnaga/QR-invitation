from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile-settings/', views.profile_settings, name='profile_seetings'),
]
