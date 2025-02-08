# Generated by Django 5.1.3 on 2024-12-15 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0006_alter_wastereporthistory_action_taken_and_more'),
        ('waste', '0010_alter_wastereport_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteReportStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('comments', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.wastereport')),
            ],
        ),
    ]
