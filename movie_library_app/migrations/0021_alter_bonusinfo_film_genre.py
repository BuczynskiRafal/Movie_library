# Generated by Django 3.2.7 on 2021-10-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_library_app', '0020_alter_bonusinfo_film_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusinfo',
            name='film_genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Comedy'), (3, 'Drama'), (0, 'Other'), (2, 'Horror'), (4, 'Action')], default=0),
        ),
    ]
