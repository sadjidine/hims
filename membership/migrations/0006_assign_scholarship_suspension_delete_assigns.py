# Generated by Django 4.2.4 on 2023-08-24 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_locality_options_and_more'),
        ('membership', '0005_assigns'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCode', models.CharField(max_length=50, unique=True, verbose_name='ID. Code')),
                ('firstName', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=32)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('dateOfBirth', models.DateField(verbose_name='Date of birth')),
                ('relationship', models.IntegerField(choices=[(0, 'Spouse'), (1, 'Child')], default=None, verbose_name='Relationship')),
                ('bloodGrp', models.IntegerField(blank=True, choices=[(0, 'A+'), (1, 'A-'), (2, 'B+'), (3, 'B-'), (4, 'AB+'), (5, 'AB-'), (6, 'O+'), (7, 'O-')], default=None, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('deceased_at', models.DateField(blank=True, null=True, verbose_name='Deceased at')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('grouping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.grouping')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.locality')),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='membership.police')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginDate', models.DateField(verbose_name='begin date')),
                ('endDate', models.DateField(verbose_name='end date')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='membership.assign')),
            ],
        ),
        migrations.CreateModel(
            name='Suspension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginDate', models.DateField(verbose_name='begin date')),
                ('endDate', models.DateField(verbose_name='end date')),
                ('reason', models.TextField(verbose_name='Suspension Reason')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='membership.assign')),
            ],
        ),
        migrations.DeleteModel(
            name='Assigns',
        ),
    ]