from django.db import models

class Sentence(models.Model):
    student_id = models.CharField(max_length=9, default='000000000')
    category_id = models.CharField(max_length=None, default='카테고리')
    question = models.CharField(max_length=None, default='질문')
    answer1 = models.TextField(max_length=None, default='답변1')
    answer2 = models.TextField(max_length=None, default='답변2')
    comment = models.TextField(max_length=None, default='진단')
    grade = models.CharField(max_length=2, default='등급')