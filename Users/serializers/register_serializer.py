from django.conf import settings
from rest_framework import serializers

from Users.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    # apellidos = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    email1 = serializers.EmailField(required=True, allow_blank=False, allow_null=False, max_length=100)
    email2 = serializers.EmailField(required=True, allow_blank=False, allow_null=False, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=6)


    class Meta:
        model = CustomUser
        fields = (
            "email1","email2", "nombre",
             "password")

    # validate -> Este metodo es la validación global
    # validate_email, validate_nombre, validate_pais, validate_edad, ... -> Validar de forma individual y personalizada

    def validate_email1(self, email):#duplicar 2 veces ?
        if "@" not in email:
            raise serializers.ValidationError("El email no es válido")
        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise serializers.ValidationError(
                "Extensiones no permitidas: [" + ", ".join(settings.EXTENSIONES_BLACKLIST) + "]")
        return email

    def validate_password(self, password):
        if not any(n.isdigit() for n in password):
            raise serializers.ValidationError("La contraseña debe de tener al menos un dígito")
        return password
    """
        attrs = {
            "email": "",
            "nombre": "",
            ...
        }
    """

    def validate(self, attrs):
        if attrs["email1"] != attrs["email2"]:
            raise serializers.ValidationError("Los emails no coinciden")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")#password1
        # validated_data.pop("password2")   xq?
        user = CustomUser.objects.create(
            email=validated_data["email"],
            nombre=validated_data["nombre"],
        )
        user.set_password(password)
        user.save()

        return user
