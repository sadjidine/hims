# Generated by Django 4.2.4 on 2023-08-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0008_remove_subscriptionplan_feescycle_and_more'),
        ('medical', '0006_degree_standing_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BloodGroup',
        ),
        migrations.DeleteModel(
            name='Standing',
        ),
        migrations.AlterField(
            model_name='practionner',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=None, max_length=1),
        ),
    ]
