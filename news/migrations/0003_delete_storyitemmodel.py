# Generated by Django 4.1.5 on 2023-01-10 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_storyitemmodel_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StoryItemModel',
        ),
    ]
