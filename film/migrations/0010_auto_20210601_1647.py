# Generated by Django 2.2.20 on 2021-06-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0009_merge_20210519_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_records',
            name='trans_valid',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_info',
            field=models.CharField(default='抱歉,暂无描述', max_length=500),
        ),
    ]
