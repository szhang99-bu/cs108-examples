# Generated by Django 3.1.7 on 2021-03-29 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_quote_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
