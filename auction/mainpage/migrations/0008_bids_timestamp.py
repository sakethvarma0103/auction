# Generated by Django 4.2.3 on 2023-10-16 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]