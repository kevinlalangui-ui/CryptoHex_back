from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        user = UserModel.objects.filter(email=username).first()#correo en principio único

        if user and user.check_password(password):#se valida la contraseña
            return user

        return None

