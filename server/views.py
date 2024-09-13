from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from server.serializers import SentenceSerializer

# Create your views here.

class Sentence(APIView):
    def post(self, request):

        data = request.data.copy()
    
        serializer = SentenceSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)