from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from server.serializers import SentenceSerializer
from server.models import Sentence

# Create your views here.

class SentenceView(APIView):
    def get(self, request):

        # 데이터베이스에서 모든 Sentence 객체 가져오기
        sentences = Sentence.objects.all()
    
        # 여러 객체를 직렬화할 경우, many=True 옵션을 추가
        serializer = SentenceSerializer(sentences, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)