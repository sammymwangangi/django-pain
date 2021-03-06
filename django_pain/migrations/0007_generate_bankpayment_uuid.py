# Generated by Django 2.0.6 on 2018-06-12 12:11

from django.db import migrations, models
import uuid


def generate_uuid(apps, schema_editor):
    BankPayment = apps.get_model('django_pain', 'BankPayment')
    for payment in BankPayment.objects.all():
        payment.uuid = uuid.uuid4()
        payment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_pain', '0006_add_bankpayment_uuid'),
    ]

    operations = [
        migrations.RunPython(generate_uuid, reverse_code=migrations.RunPython.noop),
    ]
