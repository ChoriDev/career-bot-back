from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from server.serializers import QuestionSerializer
from server.serializers import AnswerSerializer
from server.models import Question
from server.models import Answer
from server.request_func import send_post_to_fastapi

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

        # 질문 객체 가져오기
        question = Question.objects.get(pk=question_id)

        # answer1과 answer2를 안전하게 가져옴
        answer1 = request.data.get('answer1')
        answer2 = request.data.get('answer2', None)  # answer2가 없으면 None으로 설정

        # 문장 생성
        sentence = self.create_sentence(question.content, answer1, answer2)

        # 문장 생성
        sentence = self.create_sentence(question.content, answer1, answer2)

        # FastAPI로 데이터 전송
        fastapi_response = send_post_to_fastapi(sentence)

        # FastAPI 응답 처리
        if 'error' in fastapi_response:
            return Response(fastapi_response, status=status.HTTP_400_BAD_REQUEST)
        
         # Answer 객체 생성
        answer = Answer.objects.create(
            student_id=student_id,
            question_id=question,
            answer1=answer1,
            answer2=answer2,
            grade=fastapi_response.get('grade')
        )
        
        # 데이터 직렬화
        serializer = AnswerSerializer(answer)
        
        # Django에서 처리된 데이터를 반환
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def create_sentence(self, question_text, answer1, answer2):
        # 질문의 "_"를 각각의 answer로 대체하여 문장을 생성
        if answer2:
            # 두 개의 답변이 있을 경우
            return question_text.replace('_', answer1, 1).replace('_', answer2)  # 첫 번째 밑줄에 answer1, 두 번째 밑줄에 answer2
        else:
            # 하나의 답변만 있을 경우
            return question_text.replace('_', answer1)  # 밑줄을 answer1로 대체