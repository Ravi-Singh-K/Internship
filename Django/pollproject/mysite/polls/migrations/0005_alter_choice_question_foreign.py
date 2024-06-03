# Generated by Django 5.0.6 on 2024-05-23 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_choice_question_foreign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question_foreign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.question'),
        ),
    ]
