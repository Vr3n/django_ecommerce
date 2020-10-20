from django.urls import path
from .views import RegisterUserView, loginUser, logoutUser


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
]