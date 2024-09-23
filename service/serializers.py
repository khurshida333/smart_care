from .import models
from rest_framework import serializers

class ServiecSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'