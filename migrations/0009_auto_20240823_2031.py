# Generated by Django 3.2.20 on 2024-08-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eschol', '0008_auto_20240729_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuepublicationhistory',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issuepublicationhistory',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]
