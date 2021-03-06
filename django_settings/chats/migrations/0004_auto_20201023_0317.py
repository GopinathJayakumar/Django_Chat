# Generated by Django 3.1.2 on 2020-10-23 03:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20201023_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
