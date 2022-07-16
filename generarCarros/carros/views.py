from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import carros
from .serializers import carrosSerializers
from usuarios.models import users

# Create your views here.

class carrosView(APIView):

    def post(self,request,*args,**kwargs):

        serializer = carrosSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        marca = data.get("marca")
        modelo = data.get("modelo")
        color = data.get("color")
        potencia = data.get("potencia")
        año = data.get("año")
        placa = data.get("placa")
        propietario = int(request.data.get("propietario"))

        propietario = users.objects.get(id=propietario)

        carro = carros(marca=marca, modelo=modelo, color=color, potencia=potencia, año=año, placa=placa, propietario=propietario)
        carro.save()

        return Response({
            "data": {
                "marca": carro.marca,
                "modelo": carro.modelo,
                "color": carro.color,
                "caballos de fuerza": carro.potencia,
                "año": carro.año,
                "placa": carro.placa,
                "propietario": carro.propietario.nombre,
                "numero": carro.propietario.num,
                "sexo": carro.propietario.sexo,
                "edad": carro.propietario.edad,
            }
        })

    def get(self,request,*args,**kwargs):

        _carros = carros.objects.all()
        return Response({
            "data": [{
                "marca": carro.marca,
                "modelo": carro.modelo,
                "color": carro.color,
                "caballos de fuerza": carro.potencia,
                "año": carro.año,
                "placa": carro.placa,
                "propietario": carro.propietario.nombre,
                "numero": carro.propietario.num,
                "sexo": carro.propietario.sexo,
                "edad": carro.propietario.edad,
            } for carro in _carros]
        })