# Generated by Django 2.2.1 on 2021-05-19 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logobox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logobox',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]