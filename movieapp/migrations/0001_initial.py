# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('imdb_score', models.FloatField()),
                ('popularity', models.FloatField()),
                ('director', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
