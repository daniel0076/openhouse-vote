# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20160121_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='concept',
            field=models.TextField(verbose_name='設計理念'),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='logo',
            field=models.ImageField(upload_to='/tmp', verbose_name='作品圖片', default='logo/no-img.jpg'),
        ),
    ]
