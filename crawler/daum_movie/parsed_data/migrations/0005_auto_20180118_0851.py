# Generated by Django 2.0.1 on 2018-01-17 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0004_auto_20180117_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='actors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='director',
            new_name='directors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genres',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='grade',
            new_name='grades',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='nation',
            new_name='nations',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='premiere',
            new_name='premieres',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='titles',
        ),
    ]
