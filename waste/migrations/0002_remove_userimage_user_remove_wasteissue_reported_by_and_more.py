# Generated by Django 5.1.3 on 2024-11-22 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wasteissue',
            name='reported_by',
        ),
        migrations.RemoveField(
            model_name='wastereport',
            name='user',
        ),
        migrations.DeleteModel(
            name='PickupRequest',
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
        migrations.DeleteModel(
            name='WasteIssue',
        ),
        migrations.DeleteModel(
            name='WasteReport',
        ),
    ]
