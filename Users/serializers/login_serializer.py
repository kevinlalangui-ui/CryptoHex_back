from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


from Users.models import CustomUser

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, allow_blank=False,allow_null=False,required=True)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=5)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def validate_password(self, password):
        #comprobaos si no hay ningun digito
        if not any(n.isdigit() for n in password):
            raise serializers.ValidationError("La contraseña es incorrecta.")
        return password

    def validate(self, attrs):#attrs = clave-valor {"email": "kevin@gmail.com", "password": "aA123"}
        email = attrs.get('email')
        password = attrs.get('password')
        print(email)
        print(password)

        if not email:
            raise serializers.ValidationError("El correo no puede estar vacío ")

        user = CustomUser.objects.filter(email=email).first()#se hace la consulta a la BD

        if email:
            if "@" not in email:
                raise serializers.ValidationError("Email o contraseña incorrecta: 1010")
            if "=" in email:#nos blindamos contra sql injections
                raise serializers.ValidationError("Email o contraseña incorrecta: 1010")
            if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):#correos maleantes
                raise serializers.ValidationError("Email o contraseña incorrecta: 1011")

            mensaje_erorr= "Email o contraseña incorrectos"#variable que aporta seguridad al no revelar que le falta
            if not user:
                raise serializers.ValidationError(mensaje_erorr)#El usuario no existe
            else:
                if not user.check_password(password):
                    raise serializers.ValidationError(mensaje_erorr)#La contraseña no coincide
# --> exepct??
        refresh = RefreshToken.for_user(user)
        refresh["nombre"] = user.nombre
        return {
            "success": True,
            "data": {
                "nombre": user.nombre,
                "email": user.email,
                "role": user.role.nombre,
                "refreshToken": str(refresh),
                "token": str(refresh.access_token)
            }
        }
