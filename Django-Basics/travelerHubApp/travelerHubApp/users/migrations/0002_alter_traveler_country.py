# Generated by Django 5.1.6 on 2025-02-14 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='country',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^[A-Za-z]{3}')]),
        ),
    ]
