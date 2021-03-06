# Generated by Django 3.2 on 2021-11-14 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20211114_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs_comments',
            name='comment_subject',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 14, 18, 45, 15, 904781)),
        ),
        migrations.AlterField(
            model_name='blogs_comments',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 14, 18, 45, 15, 905779)),
        ),
        migrations.AlterField(
            model_name='get_in_touch',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 14, 18, 45, 15, 906776)),
        ),
    ]
