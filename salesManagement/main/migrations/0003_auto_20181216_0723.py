# Generated by Django 2.1.4 on 2018-12-16 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181216_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='unitprice',
            new_name='unit_price',
        ),
    ]