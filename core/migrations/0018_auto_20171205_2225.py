# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20171116_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrocinador',
            name='imagem',
            field=models.ImageField(upload_to=b'neabi/patrocinadores/'),
        ),
        migrations.AlterField(
            model_name='publicacoes',
            name='arquivo',
            field=models.FileField(upload_to=b'neabi/publicacoes/'),
        ),
    ]
