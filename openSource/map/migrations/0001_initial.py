# Generated by Django 4.1.5 on 2023-01-20 13:42

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
                ('name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=100)),
                ('groupe', models.CharField(max_length=5 , primary_key=True)),
            ],
        ),
    ]