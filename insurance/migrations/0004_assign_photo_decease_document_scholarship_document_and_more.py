# Generated by Django 4.2.4 on 2023-08-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_alter_plancategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='decease',
            name='document',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scholarship',
            name='document',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]