# Generated by Django 5.0.4 on 2024-05-05 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_enrolling_age_alter_enrolling_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolling',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
            preserve_default=False,
        ),
    ]
