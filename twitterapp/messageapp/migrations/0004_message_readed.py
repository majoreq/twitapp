# Generated by Django 2.1 on 2018-09-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='readed',
            field=models.BooleanField(default=False),
        ),
    ]