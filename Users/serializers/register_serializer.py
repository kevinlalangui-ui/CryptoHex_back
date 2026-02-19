from django.conf import settings
from rest_framework import serializers

from Users.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    #usuario
    nombre = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=50)
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, max_length=100)
    password1 = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=6)
    password2 = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=6)


    class Meta:
        model = CustomUser
        fields = (
            "nombre","email", "password1", "password2"
             )

    def validate_email1(self, email):#duplicar 2 veces ?
        if "@" not in email:
            raise serializers.ValidationError("El email no es válido")
        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise serializers.ValidationError(
                "Extensiones no permitidas: [" + ", ".join(settings.EXTENSIONES_BLACKLIST) + "]")
        return email

    def validate_password1(self, password):
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
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")

        user = CustomUser.objects.create(
            email=validated_data["email"],
            nombre=validated_data["nombre"],
        )
        user.set_password(password)
        user.save()

        return user
