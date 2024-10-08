# Generated by Django 5.1.1 on 2024-10-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_alter_answer_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer1',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer2',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='comment',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='grade',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='student_id',
            field=models.CharField(default=None, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]