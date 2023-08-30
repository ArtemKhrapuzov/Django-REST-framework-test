from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):  # get
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Добавление статей только для авторизованных


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):  # изменяет только автор
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)  # изменяет статей только для авторизованных


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):  # delete
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)  # удаляет статьи только админ
