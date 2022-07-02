from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.RegisterView.as_view()),
    path('users/register/', views.RegisterView.as_view()),
    path('users/login/', views.LoginView.as_view()),
    # path('users/', views.LoginView.as_view()),
    path('users/<int:user_id>/', views.RegisterDetailView.as_view())
]