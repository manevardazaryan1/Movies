# Generated by Django 4.1.2 on 2023-01-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0006_alter_movie_actors_alter_movie_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="rate",
            field=models.FloatField(),
        ),
    ]
