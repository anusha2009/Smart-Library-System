# Generated by Django 3.2.23 on 2024-01-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0004_auto_20240105_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='description',
            field=models.CharField(default='...', max_length=100),
        ),
    ]
