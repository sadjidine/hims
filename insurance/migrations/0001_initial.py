# Generated by Django 4.2.4 on 2023-08-25 10:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('label', models.CharField(max_length=255, verbose_name='Label')),
                ('validityDelay', models.PositiveIntegerField(help_text='Medical Care Validity Delay!', verbose_name='Validity')),
                ('standing', models.IntegerField(choices=[(0, '*'), (1, '**'), (2, '***'), (3, '****'), (4, '*****')], default=None, verbose_name='Standing')),
                ('delayAmount', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Delay Amount')),
                ('isGenderControl', models.BooleanField(default=True, verbose_name='Is Gender Control')),
                ('waitingPeriod', models.PositiveIntegerField(verbose_name='Waiting Period')),
                ('individualCeiling', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Individual Ceiling')),
                ('familyCeiling', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Family Ceiling')),
                ('privateCoverage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Private Coverage')),
                ('publicCoverage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Public Coverage')),
                ('publicClaim', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Public Claim')),
                ('privateClaim', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Private Claim')),
                ('claimDelay', models.PositiveIntegerField(help_text='Delay in days', verbose_name='Claim Delay')),
                ('maxClaim', models.PositiveIntegerField(help_text='Maximum number of claims allowed', verbose_name='Max Claim')),
                ('claimCeilling', models.DecimalField(decimal_places=0, help_text='Claim Ceilling Amount', max_digits=9, verbose_name='Claim Ceilling')),
                ('individualClaimCeiling', models.DecimalField(decimal_places=0, help_text='Individual Claim Ceiling Amount', max_digits=9, verbose_name='Individual Claim Ceiling')),
                ('familyClaimCeiling', models.DecimalField(decimal_places=0, help_text='Family Claim Ceiling Amount', max_digits=9, verbose_name='Family Claim Ceiling')),
                ('memberAgeLimit', models.PositiveIntegerField(help_text='Member Age Limit allowance', verbose_name='Member Age Limit')),
                ('childAgeLimit', models.PositiveIntegerField(help_text='Child Age Limit allowance', verbose_name='Child Age Limit')),
                ('additionalChild', models.PositiveIntegerField(help_text='Allowed Child Limited Number allowed!', verbose_name='Additional Child')),
                ('childMaxi', models.PositiveIntegerField(help_text='Allowed Child Limited Number allowed!', verbose_name='Maximum Child')),
                ('childMajority', models.PositiveIntegerField(help_text='Majority Age of child', verbose_name='Child Majority Age')),
                ('spouseAgeLimit', models.PositiveIntegerField(help_text='Spouse Age Limit allowance', verbose_name='Spouse Age Limit')),
                ('additionalSpouse', models.PositiveIntegerField(help_text='Allowed Spouse Limited Number allowed!', verbose_name='Additional Spouse')),
                ('spouseMaxi', models.PositiveIntegerField(help_text='Allowed Spouse Limited Number allowed!', verbose_name='Maximum Spouse')),
                ('insurancePremium', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Insurance Premium')),
                ('premiumCycle', models.IntegerField(choices=[(0, 'Daily'), (1, 'Weekly'), (2, 'Fortnight'), (3, 'Monthly'), (4, 'Quaterly'), (5, 'Half-yearly'), (6, 'Yearly')], default=None, verbose_name='Premium Cycle')),
                ('isActive', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='policies', to='core.company')),
            ],
            options={
                'unique_together': {('company', 'label')},
            },
        ),
        migrations.CreateModel(
            name='PlanCodification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicRate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Public Rate')),
                ('privateRate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Private Rate')),
                ('claimRate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Claim Rate')),
                ('individualCeiling', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Indidual Ceiling')),
                ('familyCeiling', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Family Ceiling')),
                ('ceilingAmount', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Ceiling Amount')),
                ('waitingDelay', models.PositiveIntegerField(help_text='Waiting delay in days.', verbose_name='Waiting Delay')),
                ('isStrict', models.BooleanField(default=False, verbose_name='Is strict')),
                ('isActive', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('codification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical.codification')),
                ('subscriptionPlan', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='insurance.subscriptionplan')),
            ],
            options={
                'unique_together': {('codification', 'subscriptionPlan')},
            },
        ),
        migrations.CreateModel(
            name='PlanCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'All')], default=None, verbose_name='Gender')),
                ('relationship', models.IntegerField(choices=[(0, 'Member'), (1, 'Spouse'), (2, 'Child'), (3, 'Member + Spouse'), (4, 'Member + Child'), (5, 'Spouse + Child'), (6, 'All')], default=None, verbose_name='Relationship')),
                ('isTicketDue', models.BooleanField(default=True, verbose_name='Is Ticket Due')),
                ('individualMaxiService', models.PositiveIntegerField(help_text='Maximum number services per Person', verbose_name='Maxi Svce/Person')),
                ('familyMaxiService', models.PositiveIntegerField(help_text='Maximum nummber services per family', verbose_name='Maxi Svce/Family')),
                ('personalCeiling', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Ceiling/Person')),
                ('familyCeiling', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Ceiling/Ceiling')),
                ('ageLimit', models.PositiveIntegerField(default=0, help_text='Age limitation for allowing the service', verbose_name='Age limit')),
                ('waitingDelay', models.PositiveIntegerField(help_text='Delay between two (2) services in days!', verbose_name='Waiting delay')),
                ('serviceTimeOut', models.PositiveIntegerField(help_text='Waiting delay after registering in days!', verbose_name='Timeout')),
                ('isStrict', models.BooleanField(default=False, verbose_name='Is strict')),
                ('isActive', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='medical.category')),
                ('subscriptionPlan', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='insurance.subscriptionplan')),
            ],
            options={
                'unique_together': {('category', 'subscriptionPlan')},
            },
        ),
    ]
