# Generated by Django 4.2.4 on 2023-08-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_moviedetails_movieid_alter_userdetails_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='UserID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
