# Generated by Django 4.2.4 on 2023-08-17 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_alter_speciality_options'),
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('rank', models.IntegerField(default=1)),
                ('note', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='practionner',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='practionner',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medical.speciality'),
        ),
        migrations.AlterUniqueTogether(
            name='practionner',
            unique_together={('firstName', 'lastName', 'dateOfBirth')},
        ),
    ]