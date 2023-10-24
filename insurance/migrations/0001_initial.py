# Generated by Django 4.2.4 on 2023-10-23 09:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_reference', models.CharField(blank=True, max_length=24, null=True, verbose_name='Doc. Reference')),
                ('requested_at', models.DateField(verbose_name='Requested Date')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
            ],
        ),
        migrations.CreateModel(
            name='ClainItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_center', models.CharField(max_length=255)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Decease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deceased_at', models.DateField(verbose_name='Deceased at')),
                ('document', models.FileField(upload_to='documents')),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police', models.CharField(editable=False, max_length=50, unique=True, verbose_name='Police ID.')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_code', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=12, max_length=40, prefix='', unique=True)),
                ('id_code', models.CharField(editable=False, max_length=50, unique=True, verbose_name='ID. Code')),
                ('external_id_code', models.CharField(blank=True, help_text='Set External ID for this Patient.', max_length=12, null=True, verbose_name='External ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=32)),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'A+'), (1, 'A-'), (2, 'B+'), (3, 'B-'), (4, 'AB+'), (5, 'AB-'), (6, 'O+'), (7, 'O-')], null=True)),
                ('relationship', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Spouse'), (1, 'Child')], null=True, verbose_name='Relationship')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('mobile_1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('mobile_2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('is_active', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='PlanCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'All')], default=None, verbose_name='Gender')),
                ('relationship', models.PositiveSmallIntegerField(choices=[(0, 'Member'), (1, 'Spouse'), (2, 'Child'), (3, 'Member + Spouse'), (4, 'Member + Child'), (5, 'Spouse + Child'), (6, 'All')], default=None, verbose_name='Relationship')),
                ('is_ticket_due', models.BooleanField(default=True, verbose_name='Is Ticket Due')),
                ('individual_maxi_service', models.PositiveSmallIntegerField(default=0, help_text='Maximum number services per Person', verbose_name='Maxi Svce/Person')),
                ('family_maxi_service', models.PositiveSmallIntegerField(default=0, help_text='Maximum nummber services per family', verbose_name='Maxi Svce/Family')),
                ('personal_ceiling', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Ceiling/Person')),
                ('family_ceiling', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Ceiling/Ceiling')),
                ('age_limit', models.PositiveSmallIntegerField(default=0, help_text='Age limitation for allowing the service', verbose_name='Age limit')),
                ('waiting_delay', models.PositiveSmallIntegerField(default=0, help_text='Delay between two (2) services in days!', verbose_name='Waiting delay')),
                ('service_timeOut', models.PositiveSmallIntegerField(default=0, help_text='Waiting delay after registering in days!', verbose_name='Timeout')),
                ('is_strict', models.BooleanField(default=False, verbose_name='Is strict')),
                ('is_active', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Plan Categories',
            },
        ),
        migrations.CreateModel(
            name='PlanCodification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_rate', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Public Rate')),
                ('private_rate', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Private Rate')),
                ('claim_rate', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Claim Rate')),
                ('individual_ceiling', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Indidual Ceiling')),
                ('family_ceiling', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Family Ceiling')),
                ('ceiling_cmount', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Ceiling Amount')),
                ('waiting_delay', models.PositiveSmallIntegerField(default=0, help_text='Waiting delay in days.', verbose_name='Waiting Delay')),
                ('is_strict', models.BooleanField(default=False, verbose_name='Is strict')),
                ('is_active', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='begin date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('document', models.FileField(upload_to='documents')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('patient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insurance.patient')),
            ],
            bases=('insurance.patient',),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('patient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insurance.patient')),
                ('matricule', models.CharField(blank=True, max_length=12, null=True)),
            ],
            bases=('insurance.patient',),
        ),
        migrations.CreateModel(
            name='Suspension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='begin date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('reason', models.TextField(verbose_name='Suspension Reason')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('note', models.TextField(blank=True, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='insurance.patient')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('label', models.CharField(max_length=255, verbose_name='Label')),
                ('validity_delay', models.PositiveSmallIntegerField(default=0, help_text='Medical Care Validity Delay!', verbose_name='Validity')),
                ('standing', models.IntegerField(choices=[(0, '★'), (1, '★★'), (2, '★★★'), (3, '★★★★'), (4, '★★★★★')], default=None, verbose_name='Standing')),
                ('is_gender_gontrol', models.BooleanField(default=True, verbose_name='Is Gender Control')),
                ('waiting_delay', models.PositiveSmallIntegerField(default=0, help_text='Waiting delay in days.', verbose_name='Waiting Delay')),
                ('individual_ceiling', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Individual Ceiling')),
                ('family_ceiling', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Family Ceiling')),
                ('private_coverage', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Private Coverage')),
                ('public_coverage', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Public Coverage')),
                ('public_claim', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Public Claim')),
                ('private_claim', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Private Claim')),
                ('claim_delay', models.PositiveSmallIntegerField(default=0, help_text='Delay in days', verbose_name='Claim Delay')),
                ('max_claim', models.PositiveSmallIntegerField(default=0, help_text='Maximum number of claims allowed', verbose_name='Max Claim')),
                ('claim_ceilling', models.DecimalField(decimal_places=0, default=0, help_text='Claim Ceilling Amount', max_digits=9, verbose_name='Claim Ceilling')),
                ('individual_claim_ceiling', models.DecimalField(decimal_places=0, default=0, help_text='Individual Claim Ceiling Amount', max_digits=9, verbose_name='Individual Claim Ceiling')),
                ('family_claim_ceiling', models.DecimalField(decimal_places=0, default=0, help_text='Family Claim Ceiling Amount', max_digits=9, verbose_name='Family Claim Ceiling')),
                ('member_age_limit', models.PositiveSmallIntegerField(default=0, help_text='Member Age Limit allowance', verbose_name='Member Age Limit')),
                ('child_age_limit', models.PositiveSmallIntegerField(default=0, help_text='Child Age Limit allowance', verbose_name='Child Age Limit')),
                ('additional_child', models.PositiveSmallIntegerField(default=0, help_text='Allowed Child Limited Number allowed!', verbose_name='Additional Child')),
                ('child_maxi', models.PositiveSmallIntegerField(default=0, help_text='Allowed Child Limited Number allowed!', verbose_name='Maximum Child')),
                ('child_majority', models.PositiveSmallIntegerField(default=0, help_text='Majority Age of child', verbose_name='Child Majority Age')),
                ('spouse_age_limit', models.PositiveSmallIntegerField(default=0, help_text='Spouse Age Limit allowance', verbose_name='Spouse Age Limit')),
                ('additional_spouse', models.PositiveSmallIntegerField(default=0, help_text='Allowed Spouse Limited Number allowed!', verbose_name='Additional Spouse')),
                ('spouse_maxi', models.PositiveSmallIntegerField(default=0, help_text='Allowed Spouse Limited Number allowed!', verbose_name='Maximum Spouse')),
                ('insurance_premium', models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Insurance Premium')),
                ('premium_cycle', models.IntegerField(choices=[(0, 'Daily'), (1, 'Weekly'), (2, 'Fortnight'), (3, 'Monthly'), (4, 'Quaterly'), (5, 'Half-yearly'), (6, 'Yearly')], default=None, verbose_name='Premium Cycle')),
                ('min_tolerated_amount', models.DecimalField(decimal_places=0, default=0, max_digits=6, verbose_name='Min. Tolerated Amount')),
                ('is_active', models.BooleanField(default=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='policies', to='core.company')),
            ],
        ),
    ]
