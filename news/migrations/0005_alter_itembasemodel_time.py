# Generated by Django 4.1.5 on 2023-01-10 02:24

from django.db import migrations
import helpers.model


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itembasemodel',
            name='time',
            field=helpers.model.DateTimeField(blank=True, null=True),
        ),
    ]
