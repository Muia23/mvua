# Generated by Django 3.1.3 on 2021-10-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvua', '0003_auto_20211023_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raindata',
            name='rainamt',
            field=models.IntegerField(),
        ),
    ]
