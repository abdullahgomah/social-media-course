# Generated by Django 4.2.1 on 2023-05-26 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'قسم ',
                'verbose_name_plural': 'الأقسام ',
            },
        ),
    ]
