# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20160121_0150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidates',
            options={'verbose_name': '作品列表', 'verbose_name_plural': '作品列表'},
        ),
        migrations.AlterField(
            model_name='candidates',
            name='logo',
            field=models.ImageField(verbose_name='作品圖片', default='static/logos/no.jpg', upload_to='static/logos'),
        ),
    ]
