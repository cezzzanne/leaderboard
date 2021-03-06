# Generated by Django 2.0.5 on 2020-01-11 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField()),
                ('submit_deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=150)),
                ('players', models.ManyToManyField(to='api.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_scores', to='api.CustomUser')),
                ('leaderboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_scores', to='api.Leaderboard')),
            ],
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaderboards', to='api.Team'),
        ),
    ]
