# Generated by Django 5.1.3 on 2024-11-29 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('waste', '0005_customuser_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteReportApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=20)),
                ('points_awarded', models.IntegerField(default=0)),
                ('blockchain_verified', models.BooleanField(default=False)),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='waste.wastereport')),
            ],
        ),
    ]
