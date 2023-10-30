# -*- coding: utf-8 -*-
#############################################################################
#
#    SIGEM (Société Ivoirienne d'Expertise, de Gestion et de Management.
#
#    Copyright (C) 2022-TODAY SIGEM(<https://www.sigem.pro>)
#    Author: Salifou OMBOTIMBE(<https://www.linkedin.com/in/ombotimbe-salifou-860a8044>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator

from phonenumber_field.modelfields import PhoneNumberField

from insurance.models import Company, Patient, Subscriber, Assign, Membership, Scholarship, Suspension

# Create your models here.
STAR_ONE = 0
STAR_TWO = 1
STAR_THREE = 2
STAR_FOUR = 3
STAR_FIVE = 4
STANDING_CHOICES = [
    (STAR_ONE, '*'),
    (STAR_TWO, '**'),
    (STAR_THREE, '***'),
    (STAR_FOUR, '****'),
    (STAR_FIVE, '*****')
]


class Speciality(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specialities"


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Codification(models.Model):
    code = models.CharField(max_length=4, unique=True)
    label = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.label}"

    class Meta:
        unique_together = ('code', 'category')


class Pathology(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=64, unique=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT)
    is_chronic = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = _("Pathologies")


class Nomenclature(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=64, unique=True)
    codification = models.ForeignKey(Codification, on_delete=models.PROTECT)
    coefficient = models.IntegerField(default=1)
    service_timeout = models.IntegerField(
        _('Service Timeout'), help_text=_('Service waiting delay in days.'))
    minimum_age = models.IntegerField(_('Minimum age'), help_text=_(
        'minimum age requirement allowed of this service'))
    maximum_age = models.IntegerField(_('Maximum age'), help_text=_(
        'maximum age requirement allowed of this service'))
    is_required_quantity = models.BooleanField(
        help_text="Is quantity required for this service?")
    is_price_required = models.BooleanField(
        _('Price Required'), help_text=_('Price required for this service?'), default=True)
    is_prior_agreement = models.BooleanField(_('Prior agreement'), help_text=_(
        'Prior agreement is required for this service?'), default=True)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        unique_together = ('code', 'name')


class Molecule(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MedicationType(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TherapeuticRoute(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Medication(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            help_text="International NonProprietary Name")
    code = models.CharField(
        max_length=64, help_text="International NonProprietary Code")
    dosage = models.CharField(
        max_length=64, help_text="Set the dosage of the pharmaceutical product")
    indicative_price = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    price_margin = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    product_timout = models.PositiveSmallIntegerField()
    minimum_age = models.PositiveSmallIntegerField()
    maximum_age = models.PositiveSmallIntegerField()
    molecule = models.ManyToManyField(Molecule)
    therapeutic_route = models.ForeignKey(
        TherapeuticRoute, on_delete=models.PROTECT, blank=True, null=True)
    medication_type = models.ForeignKey(
        MedicationType, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}({self.description})"

    class Meta:
        unique_together = ('name', 'medication_type', 'therapeutic_route')


class Degree(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            verbose_name=_('Degree name'))
    isA_ative = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Practitioner(models.Model):

    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = [
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    ]

    CorpReference = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=128)
    degree = models.ForeignKey(
        Degree, on_delete=models.PROTECT, null=True, blank=True)
    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=None)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    mobile = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='photos')
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.last_name} - {self.first_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        unique_together = ('first_name', 'last_name', 'date_of_birth')


class CenterType(models.Model):
    name = models.CharField(max_length=64)
    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class HealthCenter(models.Model):
    STAR_ONE = 0
    STAR_TWO = 1
    STAR_THREE = 2
    STAR_FOUR = 3
    STAR_FIVE = 4

    # MRC = 0
    # SRC = 1
    # PHARMACY = 2
    # STATUS_CHOICES = [
    #     (MRC, _('Mandatory Referral Center')),
    #     (SRC, _('Standard Referral Center')),
    #     (PHARMACY, _('Pharmacy'))
    # ]
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=32, unique=True)
    center_type = models.ForeignKey(
        CenterType, on_delete=models.RESTRICT, blank=True)
    # status = models.IntegerField(choices=STATUS_CHOICES)
    country = CountryField()
    address = models.CharField(max_length=64, null=True)
    # logo = models.ImageField(upload_to='images')
    phone_number = PhoneNumberField(blank=True, null=True)
    mobile_1 = PhoneNumberField(blank=True, null=True)
    mobile_2 = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    staff = models.ManyToManyField(Practitioner, related_name='centers')
    created_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.acronym

    class Meta:
        unique_together = ('acronym', 'country')


# class Staff(models.Model):
#     healthcenter = models.ForeignKey(HealthCenter, verbose_name=_(
#         'Health Center'), on_delete=models.RESTRICT)
#     practitioner = models.ForeignKey(Practitioner, on_delete=models.RESTRICT)
#     created_at = models.DateField(
#         _('Creation Date'), auto_now_add=True)
#     modified_at = models.DateField(_('Modified Date'), auto_now=True)
#     is_active = models.BooleanField(default=True)
#     note = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.practitioner__full_name} - {self.healthcenter__name}"

class Agreement(models.Model):
    MRC = 0
    SRC = 1
    PHARMACY = 2
    STATUS_CHOICES = [
        (MRC, _('Mandatory Referral Center')),
        (SRC, _('Standard Referral Center')),
        (PHARMACY, _('Pharmacy'))
    ]
    STANDING_CHOICES = [
        (STAR_ONE, '★'),
        (STAR_TWO, '★★'),
        (STAR_THREE, '★★★'),
        (STAR_FOUR, '★★★★'),
        (STAR_FIVE, '★★★★★')
    ]
    company = models.ForeignKey(
        Company, on_delete=models.RESTRICT, related_name='agreements')
    health_center = models.ForeignKey(
        HealthCenter, on_delete=models.RESTRICT, related_name='approvals')
    standing = models.IntegerField(
        _('Standing'), choices=STANDING_CHOICES, default=None)
    status = models.IntegerField(choices=STATUS_CHOICES)
    agreement_date = models.DateField(
        _('Agreement Date'), null=True, blank=True)
    ref_document = models.FileField(
        _('Ref. Document'), upload_to='document', null=True, blank=True)
    created_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)


class CareService(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.RESTRICT)
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.RESTRICT)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    insurance_fixed_part = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    insured_fixed_part = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    rebate = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    discount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    coverage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    is_not_check = models.BooleanField(
        default=False, help_text='This service medical code is not for check.')
    created_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nomenclature__name


class HealthCare(models.Model):

    CONSULTATION = 0
    DISPENSATION = 1
    EXPIRED = 2
    COMPLETED = 3

    STATUS_CHOICES = (
        (CONSULTATION, _('Consultation')),
        (DISPENSATION, _('Dispensation')),
        (EXPIRED, _('Expired')),
        (COMPLETED, _('Completed')),
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.RESTRICT, blank=True, null=True)
    # assign = models.ForeignKey(
    #     Assign, on_delete=models.RESTRICT, blank=True, null=True)
    doc_reference = models.CharField(
        _('Doc. Reference'), max_length=24, blank=True, null=True)
    mrc_center = models.ForeignKey(
        HealthCenter, on_delete=models.RESTRICT, related_name='mrc_center')
    src_center = models.ForeignKey(HealthCenter, on_delete=models.RESTRICT,
                                   related_name='src_center', blank=True, null=True)
    pharmacy = models.ForeignKey(HealthCenter, on_delete=models.RESTRICT,
                                 related_name='pharmacy', blank=True, null=True)
    pathology = models.ForeignKey(Pathology, on_delete=models.RESTRICT)
    status = models.PositiveBigIntegerField(
        _('Standing'), choices=STATUS_CHOICES, default=0)
    created_at = models.DateField(
        _('Creation Date'), auto_now_add=True, editable=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.patient.full_name


class CareItem(models.Model):
    health_care = models.ForeignKey(
        HealthCare, on_delete=models.RESTRICT, related_name='care_items')
    service = models.ForeignKey(
        CareService, on_delete=models.RESTRICT, blank=True, null=True)
    supplied_at = models.DateField(
        _('Supply Date'), auto_now_add=True, editable=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    created_at = models.DateField(
        _('Creation Date'), auto_now_add=True, editable=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service.nomenclature.name


class CareOnDemand(models.Model):
    health_care = models.ForeignKey(
        HealthCare, on_delete=models.RESTRICT, related_name='care_on_demand')
    care_service = models.ForeignKey(
        Nomenclature, on_delete=models.RESTRICT, limit_choices_to={'is_prior_agreement': True})
    supplied_at = models.DateField(
        _('Supply Date'), auto_now_add=True, editable=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    created_at = models.DateField(
        _('Creation Date'), auto_now_add=True, editable=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service.nomenclature.name


class MedicationItem(models.Model):
    health_care = models.ForeignKey(
        HealthCare, on_delete=models.RESTRICT, related_name='medication_items')
    pharmacy = models.ForeignKey(
        HealthCenter, on_delete=models.RESTRICT)
    supplied_at = models.DateField(
        _('Supply Date'), auto_now_add=True, editable=True)
    medication = models.ForeignKey(
        Medication, on_delete=models.RESTRICT, blank=True, null=True)
    is_substitute = models.BooleanField(default=False)
    prescribed = models.CharField(
        _('prescribed medication'), max_length=128, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    created_at = models.DateField(
        _('Creation Date'), auto_now_add=True, editable=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.medication__name
