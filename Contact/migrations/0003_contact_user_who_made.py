# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_remove_contact_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user_who_made',
            field=models.CharField(default=b'null', max_length=50),
        ),
    ]
