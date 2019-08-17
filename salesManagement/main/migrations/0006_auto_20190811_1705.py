# Generated by Django 2.1.7 on 2019-08-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190803_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statics',
            fields=[
                ('name', models.CharField(default='', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='batchstatus',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]