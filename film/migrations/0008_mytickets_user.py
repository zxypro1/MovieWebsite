# Generated by Django 2.2.20 on 2021-04-12 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0007_auto_20210409_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytickets',
            name='user',
            field=models.CharField(default='', max_length=32),
        ),
    ]