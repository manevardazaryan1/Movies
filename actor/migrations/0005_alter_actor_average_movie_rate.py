# Generated by Django 4.1.2 on 2023-01-30 09:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actor", "0004_remove_actor_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="average_movie_rate",
            field=models.DecimalField(
                decimal_places=1,
                default=0,
                max_digits=2,
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="Invalid rate number"
                    ),
                    django.core.validators.MaxValueValidator(
                        10, message="Max value is 10"
                    ),
                    django.core.validators.DecimalValidator(
                        decimal_places=1, max_digits=2
                    ),
                ],
            ),
        ),
    ]
