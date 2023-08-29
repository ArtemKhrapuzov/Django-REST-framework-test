import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel: # класс - объекты которого мы будем реализовать(преобразовывать в json строку)
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ("title", "content", "cat")

# def encode(): #Функция кодирующая в json обьекты из класса WomenModel
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomenSerializer(model) # словарь
#     print(model_sr.data)
#     json = JSONRenderer().render(model_sr.data) # байтовая строка в json формате
#     print(json)
#
#
# def decode(): # из json в объекты класса WomenModel
#     stream = io.BytesIO(b'{"title": "Angelina Jolie", "content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
