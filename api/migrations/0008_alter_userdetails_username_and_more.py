# Generated by Django 4.2.4 on 2023-08-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_userdetails_id_alter_userdetails_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='Username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]
