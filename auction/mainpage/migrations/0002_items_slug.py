# Generated by Django 4.2.3 on 2023-10-15 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
