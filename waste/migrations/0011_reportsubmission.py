# Generated by Django 5.1.3 on 2024-12-19 06:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0010_alter_wastereport_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_value', models.CharField(max_length=64, unique=True)),
                ('submission_count', models.IntegerField(default=1)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.wastereport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
