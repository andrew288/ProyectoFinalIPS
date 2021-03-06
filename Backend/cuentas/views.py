
from django.shortcuts import render
from rest_framework import generics , viewsets,status
from .models import Articulos, Perfiles, Comentarios_publicacion,Comentarios_articulo, Publicaciones, Categorias
from .serializers import PerfilesSerializer, ComentariosSerializer, PublicacionesSerializer, CategoriasSerializer ,ArticulosSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
import json 
import codecs
from django.contrib.auth.models import User
# Crear vistas.

class JsonM(TemplateView):
    def get(self, request, **kwargs):
        json_data = codecs.open('templates/datosAdolescentes.json','r','utf-8-sig')
        dataM = json.load(json_data)['Morbilidad_Adolescente']
        return JsonResponse(dataM,safe=False)
        
class JsonR(TemplateView):
    def get(self, request, **kwargs):
        json_data = codecs.open('templates/datosAdolescentes.json','r','utf-8-sig')
        dataR = json.load(json_data)['Riesgo_Adolescente']
        return JsonResponse(dataR,safe=False)

 
class JsonT(TemplateView):
    def get(self, request, **kwargs):
        json_data = codecs.open('templates/datosAdolescentes.json','r','utf-8-sig')
        dataT = json.load(json_data)['Tamizaje_Adolescente']
        return JsonResponse(dataT,safe=False)       


class home(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)



class UsuarioList(generics.ListCreateAPIView):
    """
        Clase generica para  lectura y escritura de perfiles
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Clase generica para  lectura y escritura de perfiles
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PerfilesList(generics.ListCreateAPIView):
    """
        Clase generica para  lectura y escritura de perfiles
    """
    queryset = Perfiles.objects.all()
    serializer_class = PerfilesSerializer

class PerfilesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Clase generica de perfiles, se utiliza para puntos finales de lectura, escritura y eliminaci??n
    """
    queryset = Perfiles.objects.all()
    serializer_class = PerfilesSerializer


class ArticulosList(generics.ListCreateAPIView):
    """
        Clase generica para  lectura y escritura de comentarios
    """
    queryset = Articulos.objects.all()
    serializer_class = ArticulosSerializer

class ArticulosDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Clase generica de comentarios, , se utiliza para puntos finales de lectura, escritura y eliminaci??n
    """
    queryset = Articulos.objects.all()
    serializer_class = ArticulosSerializer




class ComentariosList(generics.ListCreateAPIView):
    """
        Clase generica para  lectura y escritura de comentarios
    """
    queryset = Comentarios_articulo.objects.all()
    serializer_class = ComentariosSerializer

class ComentariosDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Clase generica de comentarios, , se utiliza para puntos finales de lectura, escritura y eliminaci??n
    """
    queryset = Comentarios_articulo.objects.all()
    serializer_class = ComentariosSerializer


class PublicacionesList(generics.ListCreateAPIView):
    """
        Clase generica para  lectura y escritura de publicaciones
    """
    queryset = Publicaciones.objects.all()
    serializer_class = PublicacionesSerializer

class PublicacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Clase generica de publicaciones, se utiliza para puntos finales de lectura, escritura y eliminaci??n 
    """
    queryset = Publicaciones.objects.all()
    serializer_class = PublicacionesSerializer


class CategoriasList(generics.ListCreateAPIView):
    """
        Clase generica para  lectura y escritura de categorias
    """
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class CategoriasDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Clase generica de categorias, se utiliza para puntos finales de lectura, escritura y eliminaci??n 
    """
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


