# Generated by Django 2.0.3 on 2018-04-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]