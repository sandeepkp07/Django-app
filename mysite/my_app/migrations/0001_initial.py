# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Marks', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Convert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('convert_from', models.CharField(default=b'INR', max_length=3, choices=[(b'INR', b'INR'), (b'USD', b'USD'), (b'EUR', b'EUR'), (b'GBP', b'GBP'), (b'IDR', b'IDR'), (b'BGN', b'BGN'), (b'ILS', b'ILS'), (b'HKD', b'HKD'), (b'SGD', b'SGD')])),
                ('convert_to', models.CharField(default=b'USD', max_length=3, choices=[(b'INR', b'INR'), (b'USD', b'USD'), (b'EUR', b'EUR'), (b'GBP', b'GBP'), (b'IDR', b'IDR'), (b'BGN', b'BGN'), (b'ILS', b'ILS'), (b'HKD', b'HKD'), (b'SGD', b'SGD')])),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=120)),
                ('tweetcount', models.CharField(max_length=100)),
            ],
        ),
    ]
