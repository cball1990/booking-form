# Generated by Django 3.0.8 on 2020-07-17 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gametype', models.CharField(choices=[('40k', '40K'), ('40kcrusade', '40K Crusade'), ('30k ', '30K'), ('killteam', 'KillTeam'), ('titanicus', 'Titanicus'), ('aos', 'AOS'), ('warcry', 'Warcry'), ('underworlds', 'Underworlds'), ('necromunda', 'Necromunda'), ('other', 'Other')], default='40k', max_length=50)),
                ('points', models.IntegerField()),
                ('skilllevel', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('pro', 'Pro'), ('absolute cheese master 9000', 'Absolute Cheese Master 9000')], default='begginer', max_length=50)),
                ('opponent', models.CharField(max_length=100)),
                ('army', models.CharField(max_length=200)),
            ],
        ),
    ]
