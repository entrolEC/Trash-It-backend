# Generated by Django 3.1.3 on 2021-10-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211009_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='spouse_name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
