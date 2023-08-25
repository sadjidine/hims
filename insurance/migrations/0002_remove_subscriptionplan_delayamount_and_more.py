# Generated by Django 4.2.4 on 2023-08-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionplan',
            name='delayAmount',
        ),
        migrations.RemoveField(
            model_name='subscriptionplan',
            name='waitingPeriod',
        ),
        migrations.AddField(
            model_name='subscriptionplan',
            name='minToleratedAmount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6, verbose_name='Min. Tolerated Amount'),
        ),
        migrations.AddField(
            model_name='subscriptionplan',
            name='waitingDelay',
            field=models.PositiveIntegerField(default=0, help_text='Waiting delay in days.', verbose_name='Waiting Delay'),
        ),
    ]
