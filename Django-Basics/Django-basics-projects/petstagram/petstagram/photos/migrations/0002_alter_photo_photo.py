# Generated by Django 5.1.7 on 2025-04-01 04:12

import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='mediafiles', validators=[petstagram.photos.validators.FileSizeValidator(5)]),
        ),
    ]
