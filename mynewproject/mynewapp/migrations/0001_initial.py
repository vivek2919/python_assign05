# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name_of_Can', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CanID', models.ForeignKey(to='mynewapp.Candidate')),
            ],
        ),
    ]
