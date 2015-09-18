# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highscore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('posted', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-score',),
            },
        ),
    ]
