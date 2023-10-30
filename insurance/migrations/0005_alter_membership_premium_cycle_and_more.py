# Generated by Django 4.2.6 on 2023-10-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_alter_membership_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='premium_cycle',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Daily'), (1, 'Weekly'), (2, 'Fortnight'), (3, 'Monthly'), (4, 'Quaterly'), (5, 'Half-yearly'), (6, 'Yearly')], default=0, verbose_name='Premium Cycle'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='standing',
            field=models.PositiveBigIntegerField(choices=[(0, '★'), (1, '★★'), (2, '★★★'), (3, '★★★★'), (4, '★★★★★')], default=0, verbose_name='Standing'),
        ),
    ]
