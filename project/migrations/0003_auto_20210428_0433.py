# Generated by Django 3.1.7 on 2021-04-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210428_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='email',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ask',
            name='phone_number',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='email',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='phone_number',
            field=models.TextField(blank=True),
        ),
    ]