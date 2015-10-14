# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0003_contact_user_who_made'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_who_made',
        ),
    ]
