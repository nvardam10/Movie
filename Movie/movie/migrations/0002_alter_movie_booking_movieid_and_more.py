# Generated by Django 4.2.4 on 2023-08-15 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_booking',
            name='MovieID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie_details'),
        ),
        migrations.AlterField(
            model_name='movie_booking',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.user_details'),
        ),
    ]
