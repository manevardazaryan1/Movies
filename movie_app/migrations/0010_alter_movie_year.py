# Generated by Django 4.1.2 on 2023-01-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0009_alter_movie_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="year",
            field=models.IntegerField(),
        ),
    ]