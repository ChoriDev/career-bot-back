from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from server.views import Sentence

# APIView로 구현한 CURD에 대한 URL
urlpatterns = [
    path('result/', Sentence.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)