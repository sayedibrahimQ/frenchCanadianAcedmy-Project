# Generated by Django 5.0.4 on 2024-05-01 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
