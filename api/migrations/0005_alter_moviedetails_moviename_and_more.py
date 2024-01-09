# Generated by Django 4.2.4 on 2023-08-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_moviedetails_movietype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedetails',
            name='Moviename',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='moviedetails',
            name='Movietype',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='Username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]