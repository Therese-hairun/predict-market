# Generated by Django 3.2.6 on 2021-11-18 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='discount',
            new_name='discount_code',
        ),
        migrations.AddField(
            model_name='invoice',
            name='discount_credit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CoupleVue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('couple', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predict.couple')),
            ],
            options={
                'db_table': 'couple_vue',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CoupleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enddatetime', models.DateTimeField()),
                ('intervaltime', models.CharField(max_length=10)),
                ('high', models.DecimalField(decimal_places=10, max_digits=50)),
                ('low', models.DecimalField(decimal_places=10, max_digits=50)),
                ('close', models.DecimalField(decimal_places=10, max_digits=50)),
                ('open', models.DecimalField(decimal_places=10, max_digits=50)),
                ('volume', models.DecimalField(decimal_places=10, max_digits=50)),
                ('couple', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predict.couple')),
            ],
            options={
                'db_table': 'couple_data',
                'managed': True,
            },
        ),
    ]
