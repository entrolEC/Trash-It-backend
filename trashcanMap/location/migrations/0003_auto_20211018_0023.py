# Generated by Django 3.1.3 on 2021-10-17 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0002_auto_20211012_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trashcan',
            old_name='author_id',
            new_name='author',
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('trashcan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trashcan', to='location.trashcan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trashcan',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', through='location.Likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
