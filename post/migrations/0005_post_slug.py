# Generated by Django 4.2.1 on 2023-05-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_p_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]