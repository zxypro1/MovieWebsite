# Generated by Django 2.2.20 on 2021-04-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='seats',
            field=models.CharField(default='[]', max_length=10000),
        ),
    ]
