# Generated by Django 4.2.4 on 2023-08-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]