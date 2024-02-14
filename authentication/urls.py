from django.urls import path, include
from . import views

app_name = "auth"
urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.signup, name="signUp"),
    path("signin", views.signIn, name="signIn"),
    path("signout", views.signout, name="signOut"),
]
