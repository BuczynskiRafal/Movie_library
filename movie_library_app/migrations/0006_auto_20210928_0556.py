# Generated by Django 3.2.7 on 2021-09-28 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_library_app', '0005_auto_20210919_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=120)),
                ('film_genre', models.PositiveSmallIntegerField(choices=[(2, 'Horror'), (0, 'Other'), (1, 'Comedy'), (4, 'Action'), (3, 'Drama')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='bonus_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_library_app.bonusinfo'),
        ),
    ]
