# Generated by Django 2.2.7 on 2019-11-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191123_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='best_answer',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
