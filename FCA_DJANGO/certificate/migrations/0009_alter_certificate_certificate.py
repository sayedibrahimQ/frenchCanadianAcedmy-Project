# Generated by Django 5.0.4 on 2024-05-01 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0008_rename__django_db_models_fields_charfield___django_db_models_fields_charfield_pdf_certificate_certif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate',
            field=models.FileField(upload_to='certificates/', verbose_name='Certificate'),
        ),
    ]
