from django.db import models

class Question(models.Model):
    id = models.SmallAutoField(primary_key=True)
    category = models.CharField(max_length=1000, blank=False, null=False, default='카테고리')
    content = models.CharField(max_length=1000, blank=False, null=False, default='질문')

class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=9, default='000000000')
    question_id = models.ForeignKey('Question', related_name='answer', on_delete=models.DO_NOTHING)
    answer1 = models.TextField(max_length=None, default='답변1')
    answer2 = models.TextField(max_length=None, default='답변2')
    comment = models.TextField(max_length=None, default='진단')
    grade = models.FloatField(default=0)