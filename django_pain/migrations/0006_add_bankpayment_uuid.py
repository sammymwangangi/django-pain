# Generated by Django 2.0.4 on 2018-06-12 08:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_pain', '0005_auto_20180606_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankpayment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
