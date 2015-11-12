# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151113_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='ques_text',
            new_name='question_text',
        ),
    ]
