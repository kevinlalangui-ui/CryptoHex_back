from django.urls import path

from Users.views import UsersView, RegisterView, LoginView

urlpatterns = [
    path('todos-usuarios/', UsersView.as_view()),
    path("registro/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),

]