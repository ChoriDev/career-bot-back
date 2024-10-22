from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from server.views import QuestionView
from server.views import AnswerView
from server.views import ResultView

# APIView로 구현한 CURD에 대한 URL
urlpatterns = [
    path('questions/', QuestionView.as_view()),
    path('students/<str:student_id>/questions/<int:question_id>/answers/', AnswerView.as_view()),
    path('students/<str:student_id>/result/', ResultView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)