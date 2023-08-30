from rest_framework import serializers
from .models import Women



class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault) #заполняет поле пользователи автоматически без права выбора
    class Meta:
        model = Women
        fields = ("title", "content", "cat", "user")

