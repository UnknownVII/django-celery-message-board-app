# Generated by Django 5.1.3 on 2024-12-18 14:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a_messageboard', '0002_sentemaillog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_on', models.DateTimeField(auto_now_add=True)),
                ('message_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='a_messageboard.messageboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]