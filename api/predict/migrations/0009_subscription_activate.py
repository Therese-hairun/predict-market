# Generated by Django 3.2.6 on 2021-12-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0008_client_customers_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='activate',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
