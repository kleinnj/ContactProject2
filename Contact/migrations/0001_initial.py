# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_first_name', models.CharField(max_length=50)),
                ('contact_last_name', models.CharField(max_length=50)),
                ('contact_phone_number', models.CharField(max_length=10)),
                ('contact_email_address', models.EmailField(max_length=50)),
                ('contact_street_address', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to='User.User')),
            ],
        ),
    ]
