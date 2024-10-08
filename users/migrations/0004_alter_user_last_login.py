# Generated by Django 5.0.7 on 2024-08-24 20:09

import django_celery_beat.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payment_link_payment_session_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                default=django_celery_beat.utils.now,
                verbose_name="Время последнего посещения",
            ),
        ),
    ]
