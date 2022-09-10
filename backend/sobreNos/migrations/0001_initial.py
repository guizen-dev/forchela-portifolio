# Generated by Django 4.1 on 2022-08-24 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DivBaixo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DivMeio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('sub_titulo', models.TextField()),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DivTopo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
            ],
        ),
    ]
