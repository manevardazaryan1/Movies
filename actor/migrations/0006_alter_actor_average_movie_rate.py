# Generated by Django 4.1.2 on 2023-01-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actor", "0005_alter_actor_average_movie_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="average_movie_rate",
            field=models.FloatField(),
        ),
    ]
