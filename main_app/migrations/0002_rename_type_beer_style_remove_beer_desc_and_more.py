# Generated by Django 4.0.3 on 2022-03-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='type',
            new_name='style',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='desc',
        ),
        migrations.AddField(
            model_name='beer',
            name='description',
            field=models.TextField(blank=True, max_length=900),
        ),
    ]