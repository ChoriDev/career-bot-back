from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from server.serializers import QuestionSerializer
from server.serializers import AnswerSerializer
from server.models import Question
from server.models import Answer

# Create your views here.

class QuestionView(APIView):
    def get(self, request):

        # 데이터베이스에서 모든 Question 객체 가져오기
        questions = Question.objects.all()
    
        # 여러 객체를 직렬화할 경우, many=True 옵션을 추가
        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class AnswerView(APIView):
    def get(self, request):

        # 데이터베이스에서 모든 Answer 객체 가져오기
        answers = Answer.objects.all()
    
        # 여러 객체를 직렬화할 경우, many=True 옵션을 추가
        serializer = AnswerSerializer(answers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, student_id, question_id):
        # 클라이언트가 보낸 데이터
        data = request.data.copy()

        data['student_id'] = student_id
        data['question_id'] = question_id

        question = Question.objects.get(pk=question_id)

        answer = Answer.objects.create(student_id=student_id, question_id=question, answer1=data['answer1'])

        if 'answer2' in data:
            answer.answer2 = data['answer2']
        
        answer.save()

        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)