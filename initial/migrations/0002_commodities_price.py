# Generated by Django 4.0.5 on 2022-09-25 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodities',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
