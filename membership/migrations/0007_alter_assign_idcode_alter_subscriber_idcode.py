# Generated by Django 4.2.4 on 2023-08-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_assign_scholarship_suspension_delete_assigns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign',
            name='idCode',
            field=models.CharField(editable=False, max_length=50, unique=True, verbose_name='ID. Code'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='idCode',
            field=models.CharField(editable=False, max_length=50, unique=True, verbose_name='ID. Code'),
        ),
    ]
