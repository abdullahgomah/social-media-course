# Generated by Django 4.2.1 on 2023-05-26 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('post', '0009_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='author.author'),
            preserve_default=False,
        ),
    ]