# Generated by Django 2.2.1 on 2021-05-20 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logobox', '0003_alter_logobox_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logobox',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
