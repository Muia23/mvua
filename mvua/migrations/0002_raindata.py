# Generated by Django 3.1.3 on 2021-10-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvua', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayname', models.CharField(max_length=100)),
                ('rainamt', models.IntegerField()),
            ],
        ),
    ]
