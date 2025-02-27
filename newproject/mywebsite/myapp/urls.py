from django.urls import path
from .views import login_view, logoutuser, index

urlpatterns = [
    path("", index, name="home"),  
    path("login/", login_view, name="login"),
    path("logout/", logoutuser, name="logout"),
]
