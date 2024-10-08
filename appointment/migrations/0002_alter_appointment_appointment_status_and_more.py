# Generated by Django 5.0.6 on 2024-09-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(choices=[('Running', 'Running'), ('Completed', 'Completed'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_types',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10),
        ),
    ]
