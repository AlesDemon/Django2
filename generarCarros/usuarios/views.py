from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import users
from .serializers import userSerializers

# Create your views here.

class userView(APIView):
    
    def post(self,request,*args,**kwargs):

        serializer = userSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        propietario = data.get("nombre")
        numero = data.get("num")
        sexo = data.get("sexo")
        edad = data.get("edad")

        usuarios = users(nombre=propietario, num=numero, sexo=sexo, edad=edad)
        usuarios.save()

        return Response({
            "data":[{
                "propietario" : usuarios.nombre,
                "numero" : usuarios.num,
                "sexo" : usuarios.sexo,
                "edad" : usuarios.edad,
                "id": usuarios.id,
            }]
        })

    def get(self,request,*args,**kwargs):

        _usuarios = users.objects.all()

        return Response({
            "data":[{
                "propietario" : usuarios.nombre,
                "numero" : usuarios.num,
                "sexo" : usuarios.sexo,
                "edad" : usuarios.edad,
                "id": usuarios.id,
            } for usuarios in _usuarios]
        })