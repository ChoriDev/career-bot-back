from django.db import models

class Question(models.Model):
    id = models.SmallAutoField(primary_key=True)
    category = models.CharField(max_length=1000, blank=False, null=True, default=None)
    content = models.CharField(max_length=1000, blank=False, null=True, default=None)

class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=9, null=True, default=None)
    question_id = models.ForeignKey('Question', related_name='answer', on_delete=models.DO_NOTHING, db_column='question_id')
    answer1 = models.TextField(max_length=None, null=True, default=None)
    answer2 = models.TextField(max_length=None, null=True, default=None)
    comment = models.TextField(max_length=None, null=True, default=None)
    grade = models.FloatField(null=True, default=None)