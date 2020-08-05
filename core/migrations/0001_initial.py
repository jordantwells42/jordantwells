# Generated by Django 3.0.8 on 2020-08-05 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('description', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=7)),
                ('ref', models.CharField(max_length=31)),
            ],
        ),
    ]