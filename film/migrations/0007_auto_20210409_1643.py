# Generated by Django 2.2.20 on 2021-04-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0006_auto_20210409_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysite',
            name='moviename',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='mytickets',
            name='moviename',
            field=models.CharField(default='', max_length=32),
        ),
    ]
