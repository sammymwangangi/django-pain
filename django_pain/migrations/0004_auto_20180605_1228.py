# Generated by Django 2.0.4 on 2018-06-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_pain', '0003_auto_20180515_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentsymbols',
            name='payment',
        ),
        migrations.AddField(
            model_name='bankpayment',
            name='constant_symbol',
            field=models.CharField(blank=True, max_length=10, verbose_name='Constant symbol'),
        ),
        migrations.AddField(
            model_name='bankpayment',
            name='specific_symbol',
            field=models.CharField(blank=True, max_length=10, verbose_name='Specific symbol'),
        ),
        migrations.AddField(
            model_name='bankpayment',
            name='variable_symbol',
            field=models.CharField(blank=True, max_length=10, verbose_name='Variable symbol'),
        ),
        migrations.DeleteModel(
            name='PaymentSymbols',
        ),
    ]
