# Generated by Django 5.1.7 on 2025-03-11 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Truenewsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Truenewsapp.author', verbose_name='Автор'),
        ),
    ]
