# Generated by Django 5.1.4 on 2025-01-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date completed'),
        ),
    ]