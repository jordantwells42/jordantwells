# Generated by Django 3.0.8 on 2020-08-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='Lol', max_length=255),
            preserve_default=False,
        ),
    ]