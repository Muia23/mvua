# Generated by Django 3.1.3 on 2021-10-23 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvua', '0002_raindata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raindata',
            name='rainamt',
            field=models.CharField(max_length=100),
        ),
    ]
