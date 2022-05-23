from dataclasses import fields
from rest_framework import serializers
from .models import Book

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'