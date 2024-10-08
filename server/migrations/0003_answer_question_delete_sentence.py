# Generated by Django 5.1.1 on 2024-10-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_rename_category_id_sentence_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='000000000', max_length=9)),
                ('category', models.CharField(default='카테고리', max_length=1000)),
                ('question', models.CharField(default='질문', max_length=1000)),
                ('answer1', models.TextField(default='답변1')),
                ('answer2', models.TextField(default='답변2')),
                ('comment', models.TextField(default='진단')),
                ('grade', models.CharField(default='등급', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='카테고리', max_length=1000)),
                ('content', models.CharField(default='질문', max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Sentence',
        ),
    ]
