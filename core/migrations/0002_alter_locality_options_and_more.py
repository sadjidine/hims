# Generated by Django 4.2.4 on 2023-08-16 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locality',
            options={'verbose_name_plural': 'Localities'},
        ),
        migrations.RenameField(
            model_name='district',
            old_name='active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='exercice',
            old_name='active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='grouping',
            old_name='active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='locality',
            old_name='active',
            new_name='isActive',
        ),
    ]
