# Generated by Django 2.1.7 on 2019-03-06 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0003_auto_20190305_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]