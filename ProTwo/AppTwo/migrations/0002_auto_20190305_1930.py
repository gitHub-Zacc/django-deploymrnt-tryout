# Generated by Django 2.1.7 on 2019-03-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.CharField(max_length=30),
        ),
    ]
