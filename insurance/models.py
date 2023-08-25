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
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import Company
from medical.models import Category, Codification


# Create your models here.
class SubscriptionPlan(models.Model):

    DAY = 0
    WEEK = 1
    FORTNIGHT = 2
    MONTH = 3
    QUATER = 4
    HALFYEAR = 5
    YEAR = 6

    FEES_CYCLE_CHOICES = [
        (DAY, _('Daily')),
        (WEEK, _('Weekly')),
        (FORTNIGHT, _('Fortnight')),
        (MONTH, _('Monthly')),
        (QUATER, _('Quaterly')),
        (HALFYEAR, _('Half-yearly')),
        (YEAR, _('Yearly')),
    ]

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

    name = models.CharField(_('Name'), max_length=64)
    label = models.CharField(_('Label'), max_length=255)
    company = models.ForeignKey(
        Company, on_delete=models.RESTRICT, related_name='policies')
    validityDelay = models.PositiveIntegerField(
        _('Validity'), help_text='Medical Care Validity Delay!')
    standing = models.IntegerField(
        _('Standing'), choices=STANDING_CHOICES, default=None)
    delayAmount = models.DecimalField(
        _('Delay Amount'), max_digits=6, decimal_places=0)
    isGenderControl = models.BooleanField(_('Is Gender Control'), default=True)
    waitingPeriod = models.PositiveIntegerField(_('Waiting Period'))
    individualCeiling = models.DecimalField(
        _('Individual Ceiling'), max_digits=9, decimal_places=0)
    familyCeiling = models.DecimalField(
        _('Family Ceiling'), max_digits=9, decimal_places=0)
    publicCoverage = models.PositiveIntegerField(_('Public Coverage'), validators=[
                                                 MinValueValidator(0), MaxValueValidator(100)])
    privateCoverage = models.PositiveIntegerField(_('Private Coverage'), validators=[
                                                  MinValueValidator(0), MaxValueValidator(100)])
    publicCoverage = models.PositiveIntegerField(_('Public Coverage'), validators=[
                                                 MinValueValidator(0), MaxValueValidator(100)])
    publicClaim = models.PositiveIntegerField(_('Public Claim'), validators=[MinValueValidator(
        0), MaxValueValidator(100)])  # Remboursement Public Zone couverte
    privateClaim = models.PositiveIntegerField(_('Private Claim'), validators=[MinValueValidator(
        0), MaxValueValidator(100)])  # Remboursement Privé Zone couverte
    claimDelay = models.PositiveIntegerField(
        _('Claim Delay'), help_text='Delay in days')
    maxClaim = models.PositiveIntegerField(
        _('Max Claim'), help_text='Maximum number of claims allowed')
    claimCeilling = models.DecimalField(
        _('Claim Ceilling'), max_digits=9, decimal_places=0, help_text='Claim Ceilling Amount')
    individualClaimCeiling = models.DecimalField(
        _('Individual Claim Ceiling'), max_digits=9, decimal_places=0, help_text='Individual Claim Ceiling Amount')
    familyClaimCeiling = models.DecimalField(
        _('Family Claim Ceiling'), max_digits=9, decimal_places=0, help_text='Family Claim Ceiling Amount')
    memberAgeLimit = models.PositiveIntegerField(
        _('Member Age Limit'), help_text='Member Age Limit allowance')
    childAgeLimit = models.PositiveIntegerField(
        _('Child Age Limit'), help_text='Child Age Limit allowance')
    additionalChild = models.PositiveIntegerField(
        _('Additional Child'), help_text=_('Allowed Child Limited Number allowed!'))
    childMaxi = models.PositiveIntegerField(
        _('Maximum Child'), help_text=_('Allowed Child Limited Number allowed!'))
    childMajority = models.PositiveIntegerField(
        _('Child Majority Age'), help_text='Majority Age of child')
    spouseAgeLimit = models.PositiveIntegerField(
        _('Spouse Age Limit'), help_text='Spouse Age Limit allowance')
    additionalSpouse = models.PositiveIntegerField(
        _('Additional Spouse'), help_text=_('Allowed Spouse Limited Number allowed!'))
    spouseMaxi = models.PositiveIntegerField(
        _('Maximum Spouse'), help_text=_('Allowed Spouse Limited Number allowed!'))
    insurancePremium = models.DecimalField(
        _('Insurance Premium'), max_digits=9, decimal_places=0)
    premiumCycle = models.IntegerField(
        _('Premium Cycle'), choices=FEES_CYCLE_CHOICES, default=None)
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.label

    class Meta:
        unique_together = ('company', 'label')


class PlanCategory(models.Model):
    MALE = 0
    FEMALE = 1
    ALL = 2
    GENDER_CHOICES = [
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (ALL, _('All')),
    ]

    MEMBER = 0
    SPOUSE = 1
    CHILD = 2
    MEMBER_SPOUSE = 3
    MEMBER_CHILD = 4
    SPOUSE_CHILD = 5
    ALL = 6

    RELATIONSHIP_CHOICES = [
        (MEMBER, _('Member')),
        (SPOUSE, _('Spouse')),
        (CHILD, _('Child')),
        (MEMBER_SPOUSE, _('Member + Spouse')),
        (MEMBER_CHILD, _('Member + Child')),
        (SPOUSE_CHILD, _('Spouse + Child')),
        (ALL, _('All'))
    ]

    subscriptionPlan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    gender = models.IntegerField(
        _('Gender'), choices=GENDER_CHOICES, default=None)
    relationship = models.IntegerField(
        _('Relationship'), choices=RELATIONSHIP_CHOICES, default=None)
    isTicketDue = models.BooleanField(_('Is Ticket Due'), default=True)
    individualMaxiService = models.PositiveIntegerField(
        _('Maxi Svce/Person'), help_text=_('Maximum number services per Person'))
    familyMaxiService = models.PositiveIntegerField(
        _('Maxi Svce/Family'), help_text=_('Maximum nummber services per family'))
    personalCeiling = models.DecimalField(
        _('Ceiling/Person'), max_digits=9, decimal_places=0)
    familyCeiling = models.DecimalField(
        _('Ceiling/Ceiling'), max_digits=9, decimal_places=0)
    ageLimit = models.PositiveIntegerField(_('Age limit'), help_text=_(
        'Age limitation for allowing the service'), default=0)
    waitingDelay = models.PositiveIntegerField(_('Waiting delay'), help_text=_(
        'Delay between two (2) services in days!'))
    serviceTimeOut = models.PositiveIntegerField(_('Timeout'), help_text=_(
        'Waiting delay after registering in days!'))
    sStrict = models.BooleanField(_('Is strict'), default=False)
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.category.name

    class Meta:
        unique_together = ('category', 'subscriptionPlan')


class PlanCodification(models.Model):
    subscriptionPlan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.RESTRICT)
    codification = models.ForeignKey(Codification, on_delete=models.RESTRICT)
    publicRate = models.PositiveIntegerField(_('Public Rate'), validators=[
                                             MinValueValidator(1), MaxValueValidator(100)])
    privateRate = models.PositiveIntegerField(_('Private Rate'), validators=[
                                              MinValueValidator(1), MaxValueValidator(100)])
    claimRate = models.PositiveIntegerField(_('Claim Rate'), validators=[
                                            MinValueValidator(1), MaxValueValidator(100)])
    individualCeiling = models.DecimalField(
        _('Indidual Ceiling'), max_digits=9, decimal_places=0)
    familyCeiling = models.DecimalField(
        _('Family Ceiling'), max_digits=9, decimal_places=0)
    ceilingAmount = models.DecimalField(
        _('Ceiling Amount'), max_digits=9, decimal_places=0)
    waitingDelay = models.PositiveIntegerField(
        _('Waiting Delay'), help_text=_('Waiting delay in days.'))
    isStrict = models.BooleanField(_('Is strict'), default=False)
    note = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.codification.code

    class Meta:
        unique_together = ('codification', 'subscriptionPlan')
