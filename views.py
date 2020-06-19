from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from.models import stock
from.serializer import stockserializer
@api_view(["GET","POST"])
#listall stocks that is get function
def show_list(request):
        if(request.method=="GET"):
            stocks=stock.objects.all()
            serializer=stockserializer(stocks,many=True)
            return Response(serializer.data)
        elif(request.method=='POST'):
            serializer=stockserializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status= status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
