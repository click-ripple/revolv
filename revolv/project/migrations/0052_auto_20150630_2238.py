# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0051_project_people_affected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='people_affected',
            field=models.PositiveIntegerField(default=0, help_text=b'How many people will be impacted by this project?'),
            preserve_default=True,
        ),
    ]
