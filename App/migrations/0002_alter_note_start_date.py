# Generated by Django 4.1.7 on 2023-03-02 07:13

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
