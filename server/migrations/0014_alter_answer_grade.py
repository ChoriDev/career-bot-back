# Generated by Django 5.1.2 on 2024-10-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_alter_answer_answer1_alter_answer_answer2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='grade',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
