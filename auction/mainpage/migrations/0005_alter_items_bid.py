# Generated by Django 4.2.3 on 2023-10-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_alter_items_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='bid',
            field=models.IntegerField(default=0),
        ),
    ]
