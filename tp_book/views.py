from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from tp_book.models import Book
from tp_book.serializers import BookModelSerializer
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
import math

class PostModelData(APIView):   
    def post(self,request):
        serializers = BookModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllData(APIView):

    def get(self, request, pk, format=None):

        #user = request.user
        event = Book.objects.get(pk=pk)
        news = Book.objects.all()

         # -----------------------------------------------------------
        page_number = self.request.content_params.get('page_number ', pk)
        page_size = self.request.content_params.get('page_size ', 2)

        paginator = Paginator(news , page_size)
        if (page_number < math.ceil(paginator.count/page_size)+1):
            serializer = BookModelSerializer(paginator.page(page_number) , many=True, context={'request':request})
            # ----------------------------------------------------------- 
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)