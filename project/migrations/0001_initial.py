# Generated by Django 3.1.7 on 2021-04-15 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('year', models.TextField(blank=True)),
                ('manufacturer', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('phone_number', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('sold', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.computerparts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('sold', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.computerparts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.user')),
            ],
        ),
    ]