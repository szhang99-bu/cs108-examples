# Generated by Django 3.1.7 on 2021-03-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('city', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
    ]
