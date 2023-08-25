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
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specialities"


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Codification(models.Model):
    code = models.CharField(max_length=4, unique=True)
    label = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

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
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = _("Pathologies")


class Nomenclature(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=64, unique=True)
    codification = models.ForeignKey(Codification, on_delete=models.PROTECT)
    coefficient = models.IntegerField(default=1)
    serviceTimeout = models.IntegerField(
        _('Service Timeout'), help_text=_('Service waiting delay in days.'))
    minimumAge = models.IntegerField(_('Minimum age'), help_text=_(
        'minimum age requirement allowed of this service'))
    maximumAge = models.IntegerField(_('Maximum age'), help_text=_(
        'maximum age requirement allowed of this service'))
    isRequiredQuantity = models.BooleanField(
        help_text="Is quantity required for this service?")
    isPriceRequired = models.BooleanField(
        _('Price Required'), help_text=_('Price required for this service?'), default=True)
    isPriorAgreement = models.BooleanField(_('Prior agreement'), help_text=_(
        'Prior agreement is required for this service?'))
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        unique_together = ('code', 'name')


class Molecule(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MedicationType(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TherapeuticRoute(models.Model):
    name = models.CharField(max_length=64, unique=True)
    note = models.TextField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Medication(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            help_text="International NonProprietary Name")
    code = models.CharField(
        max_length=64, help_text="International NonProprietary Code")
    dosage = models.CharField(
        max_length=64, help_text="Set the dosage of the pharmaceutical product")
    indicativePrice = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    priceMargin = models.DecimalField(
        max_digits=9, decimal_places=0, default=0)
    waitingPeriod = models.PositiveSmallIntegerField()
    minimumAge = models.PositiveSmallIntegerField()
    maximumAge = models.PositiveSmallIntegerField()
    molecule = models.ManyToManyField(Molecule)
    therapeuticRoute = models.ForeignKey(
        TherapeuticRoute, on_delete=models.PROTECT, blank=True, null=True)
    medicationType = models.ForeignKey(
        MedicationType, on_delete=models.PROTECT)
    isActive = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}({self.descrcodeiption})"

    class Meta:
        unique_together = ('name', 'medicationType', 'therapeuticRoute')


class Degree(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            verbose_name=_('Degree name'))
    isActive = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Practionner(models.Model):

    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = [
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    ]

    CorpReference = models.CharField(max_length=32)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=128)
    degree = models.ForeignKey(
        Degree, on_delete=models.PROTECT, null=True, blank=True)
    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=None)
    dateOfBirth = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.lastName} - {self.firstName}"

    class Meta:
        unique_together = ('firstName', 'lastName', 'dateOfBirth')


class HealthCenter(models.Model):
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=32, unique=True)
    country = CountryField()
    address = models.CharField(max_length=64, null=True)
    # logo = models.ImageField(upload_to='images')
    mobile = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    staff = models.ManyToManyField(Practionner, blank=True)
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    isActive = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.acronym

    class Meta:
        unique_together = ('acronym', 'country')


class Service(models.Model):
    healthcenter = models.ForeignKey(
        HealthCenter, on_delete=models.RESTRICT, related_name='services')
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.RESTRICT)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    insurancePart = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    insuredPart = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    isActive = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)
