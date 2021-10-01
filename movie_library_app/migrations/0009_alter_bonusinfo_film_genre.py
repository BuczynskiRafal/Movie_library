# Generated by Django 3.2.7 on 2021-10-01 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_library_app', '0008_auto_20210929_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusinfo',
            name='film_genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Comedy'), (3, 'Drama'), (2, 'Horror'), (4, 'Action'), (0, 'Other')], default=0),
        ),
    ]
