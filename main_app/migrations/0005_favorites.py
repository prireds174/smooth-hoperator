# Generated by Django 4.0.3 on 2022-03-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_beer_created_at_remove_beer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('brand', models.CharField(max_length=120)),
                ('img', models.CharField(max_length=250)),
                ('style', models.CharField(max_length=90)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
