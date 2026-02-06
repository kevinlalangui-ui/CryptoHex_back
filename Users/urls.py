from django.urls import path

from Users.views import UsersView, RegisterView

urlpatterns = [
    path('todos-usuarios/', UsersView.as_view()),
    path("registro/", RegisterView.as_view()),
]