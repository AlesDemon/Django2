from rest_framework import serializers

class carrosSerializers(serializers.Serializer):

    marca = serializers.CharField()
    modelo = serializers.CharField()
    color = serializers.CharField()
    potencia = serializers.IntegerField()
    año = serializers.IntegerField()
    placa = serializers.CharField()

    def validate(self, data):

        num = "1234567890"

        for number in num:
            if number in data["marca"]:
                raise serializers.ValidationError("Marca no valida")
                
        for number in num:
            if number in data["color"]:
                raise serializers.ValidationError("Color no valido")

        return data