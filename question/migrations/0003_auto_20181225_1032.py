# Generated by Django 2.1.3 on 2018-12-25 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_availablelanguage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.AvailableLanguage'),
        ),
    ]
