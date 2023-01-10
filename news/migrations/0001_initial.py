# Generated by Django 4.1.5 on 2023-01-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoryItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hnId', models.PositiveIntegerField(blank=True, null=True, verbose_name='HackerNews Id')),
                ('by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Author')),
                ('deleted', models.BooleanField(default=False, null=True, verbose_name='Deleted')),
                ('dead', models.BooleanField(default=False, null=True, verbose_name='Dead')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('kids', models.TextField(blank=True, null=True, verbose_name='Kids')),
                ('_type', models.CharField(default='story', max_length=10, verbose_name='Type')),
                ('title', models.CharField(blank=True, max_length=225, null=True, verbose_name='Title')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Url')),
                ('descendants', models.PositiveIntegerField(blank=True, null=True, verbose_name='Descendants')),
                ('score', models.PositiveIntegerField(blank=True, null=True, verbose_name='Score')),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
            },
        ),
    ]