# Generated by Django 4.2.4 on 2023-08-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_moviedetails_id_alter_moviedetails_movieid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='Movieprice',
            field=models.IntegerField(default=100),
        ),
    ]
