from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class LoginView(APIView):
    permission_classes = [AllowAny] #no hace falta estr autenticado para en
                                    #entrar a esta vista
    pass