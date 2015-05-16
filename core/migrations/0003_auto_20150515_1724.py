# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150514_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='google_plus',
            field=models.URLField(default=datetime.datetime(2015, 5, 15, 17, 24, 6, 364293, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='twitter',
            field=models.URLField(default=datetime.datetime(2015, 5, 15, 17, 24, 15, 948114, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
