# Generated by Django 5.1.3 on 2024-11-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='newsletter_subscribed',
            field=models.BooleanField(default=True),
        ),
    ]
