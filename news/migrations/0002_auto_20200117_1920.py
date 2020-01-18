# Generated by Django 3.0.2 on 2020-01-17 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='date', verbose_name='New title')),
                ('description', models.TextField(verbose_name='Short content')),
                ('content', models.TextField(verbose_name='All information')),
                ('date', models.DateField(db_index=True, default=datetime.datetime(2020, 1, 17, 19, 20, 26, 499518), verbose_name='Published')),
            ],
            options={
                'verbose_name': 'new',
                'verbose_name_plural': 'news',
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]