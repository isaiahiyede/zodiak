# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0063_auto_20190217_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minibatches',
            options={'verbose_name_plural': 'Mini Batches', 'ordering': ['-batch_created_on']},
        ),
        migrations.RemoveField(
            model_name='job',
            name='no_of_arrival_batches',
        ),
    ]
