# Generated by Django 4.0.5 on 2022-06-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
