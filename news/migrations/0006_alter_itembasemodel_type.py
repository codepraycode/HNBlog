# Generated by Django 4.1.5 on 2023-01-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_itembasemodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itembasemodel',
            name='type',
            field=models.CharField(choices=[('job', 'JOB'), ('story', 'STORY'), ('comment', 'COMMENT')], default='story', max_length=10, verbose_name='Type'),
        ),
    ]
