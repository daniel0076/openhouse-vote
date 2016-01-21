# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_auto_20160121_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='logo',
            field=models.ImageField(verbose_name='作品圖片', upload_to='/tmp'),
        ),
    ]
