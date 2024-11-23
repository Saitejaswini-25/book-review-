# Generated by Django 5.1.2 on 2024-10-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('accessToken', models.CharField(blank=True, null=True)),
                ('refreshToken', models.CharField(blank=True, null=True)),
                ('tokenExpiry', models.DateTimeField(blank=True, null=True)),
                ('creationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]