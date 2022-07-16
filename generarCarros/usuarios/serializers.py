from rest_framework import serializers

class userSerializers(serializers.Serializer):

    nombre = serializers.CharField()
    num = serializers.IntegerField()
    sexo = serializers.CharField()
    edad = serializers.IntegerField()

    def validate(self, data):
        
        num = "1234567890"

        for number in num:
            if number in data["nombre"]:
                raise serializers.ValidationError("Nombre no valido")

        return data