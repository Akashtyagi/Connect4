# Generated by Django 3.1.1 on 2020-09-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameboard',
            name='id',
        ),
        migrations.AlterField(
            model_name='gameboard',
            name='token',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]