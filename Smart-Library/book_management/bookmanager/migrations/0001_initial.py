# Generated by Django 3.2.23 on 2024-01-01 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_number', models.IntegerField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_number', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelves', to='bookmanager.librarylevel')),
            ],
            options={
                'unique_together': {('level', 'shelf_number')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='bookmanager.shelf')),
            ],
        ),
    ]
