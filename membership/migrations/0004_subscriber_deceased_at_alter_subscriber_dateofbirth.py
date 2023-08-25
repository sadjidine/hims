# Generated by Django 4.2.4 on 2023-08-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_subscriber_email_subscriber_mobile_police'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='deceased_at',
            field=models.DateField(blank=True, null=True, verbose_name='Deceased at'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='dateOfBirth',
            field=models.DateField(verbose_name='Date of birth'),
        ),
    ]
