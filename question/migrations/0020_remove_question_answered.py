# Generated by Django 2.2.7 on 2019-11-24 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0019_question_answered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answered',
        ),
    ]