# Generated by Django 2.2.7 on 2019-11-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rating_user',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
