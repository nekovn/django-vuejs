# Generated by Django 3.2.3 on 2021-05-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logobox', '0002_auto_20210519_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logobox',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
