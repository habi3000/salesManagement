# Generated by Django 2.1.4 on 2018-12-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181216_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='profit',
        ),
        migrations.AddField(
            model_name='sales',
            name='totalprofit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sales',
            name='unitprofit',
            field=models.FloatField(default=0.0),
        ),
    ]