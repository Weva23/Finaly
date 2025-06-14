# Generated by Django 5.1.7 on 2025-05-05 14:31

import consultants.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0003_documentcategory_documentged_documentaccess_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentged',
            name='folder_type',
            field=models.CharField(choices=[('ADMIN', 'Dossier administratif'), ('TECHNIQUE', 'Dossier technique'), ('FINANCE', 'Dossier financier'), ('CONTEXTE', 'Contexte'), ('OUTREACH', 'Outreach'), ('GENERAL', 'Général')], default='GENERAL', max_length=20),
        ),
        migrations.AlterField(
            model_name='documentged',
            name='file',
            field=models.FileField(upload_to=consultants.models.DocumentGED.get_upload_path),
        ),
    ]
