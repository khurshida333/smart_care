# Generated by Django 5.0.6 on 2024-09-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_alter_appointment_appointment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_types',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10),
        ),
    ]
