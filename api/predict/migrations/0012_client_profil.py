# Generated by Django 3.2.6 on 2021-12-29 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0011_alter_couple_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='profil',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='user_profile'),
        ),
    ]
