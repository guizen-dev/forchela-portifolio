# Generated by Django 4.1 on 2022-08-30 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_footer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='divbaixo',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='divinformacao',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='divmeio',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='divtopo',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='footer',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
