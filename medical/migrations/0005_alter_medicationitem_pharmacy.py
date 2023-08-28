# Generated by Django 4.2.4 on 2023-08-28 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0004_healthcenter_status_medicationitem_pharmacy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationitem',
            name='pharmacy',
            field=models.ForeignKey(limit_choices_to={'status': 2}, on_delete=django.db.models.deletion.RESTRICT, to='medical.healthcenter'),
        ),
    ]