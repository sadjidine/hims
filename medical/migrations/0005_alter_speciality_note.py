# Generated by Django 4.2.4 on 2023-08-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0004_alter_bloodgroup_note_alter_category_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]