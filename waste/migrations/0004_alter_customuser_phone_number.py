# Generated by Django 5.1.3 on 2024-11-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0003_wastereport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
