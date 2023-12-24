# Generated by Django 4.2.8 on 2023-12-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('avatar', models.URLField(blank=True, verbose_name='avatar')),
                ('desc', models.TextField(blank=True, max_length=300)),
                ('status', models.CharField(choices=[('online', 'online'), ('offline', 'offline'), ('do not disturb', 'do not disturb')], default='online', max_length=18, verbose_name='status')),
            ],
        ),
    ]