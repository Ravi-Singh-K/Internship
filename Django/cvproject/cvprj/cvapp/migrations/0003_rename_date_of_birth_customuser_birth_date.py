# Generated by Django 5.0.6 on 2024-06-06 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
    ]
