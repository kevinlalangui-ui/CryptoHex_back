from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import CustomUser


class UsersView(APIView):
    permission_classes = [AllowAny]
 #obtenemos todos los objetos, en una lista guradamos nombre y email
    def get(self, request):
        users = CustomUser.objects.all()

        data = []
        for user in users:
            data.append({
                'nombre': user.nombre,
                'email': user.email,
            })
#en otro solo el nombre
        data2 = [{'nombre': u.nombre} for u in users]

        return Response({'data': data}, status=status.HTTP_200_OK)






