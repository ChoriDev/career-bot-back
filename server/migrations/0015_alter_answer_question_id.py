# Generated by Django 5.1.2 on 2024-10-22 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_alter_answer_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(db_column='question', on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='server.question'),
        ),
    ]
