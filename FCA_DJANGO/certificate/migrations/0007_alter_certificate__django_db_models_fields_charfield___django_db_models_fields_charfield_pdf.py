# Generated by Django 5.0.4 on 2024-04-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0006_remove_certificate_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='<django.db.models.fields.CharField>_<django.db.models.fields.CharField>.pdf',
            field=models.FileField(upload_to='media/certificates/', verbose_name='Certificate'),
        ),
    ]
