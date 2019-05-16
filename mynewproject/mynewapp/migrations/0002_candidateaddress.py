# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynewapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Address', models.CharField(unique=True, max_length=100)),
            ],
        ),
    ]
