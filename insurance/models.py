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

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

from core.models import Company, Locality, Grouping
# from medical.models import MedicineCategory, Codification

# Create your models here.
GENDER_MALE = 0
GENDER_FEMALE = 1

GENDER_CHOICES = (
    (GENDER_MALE, _('Male')),
    (GENDER_FEMALE, _('Female')),
)

POSITIVE_A = 0
NEGATIVE_A = 1
POSITIVE_B = 2
NEGATIVE_B = 3
POSITIVE_AB = 4
NEGATIVE_AB = 5
POSITIVE_O = 6
NEGATIVE_O = 7

BLOOD_GRP_CHOICES = [
    (POSITIVE_A, 'A+'),
    (NEGATIVE_A, 'A-'),
    (POSITIVE_B, 'B+'),
    (NEGATIVE_B, 'B-'),
    (POSITIVE_AB, 'AB+'),
    (NEGATIVE_AB, 'AB-'),
    (POSITIVE_O, 'O+'),
    (NEGATIVE_O, 'O-'),

]


class SubscriptionPlan(models.Model):

    DAY = 0
    WEEK = 1
    FORTNIGHT = 2
    MONTH = 3
    QUATER = 4
    HALFYEAR = 5
    YEAR = 6

    PREMIUM_CYCLE_CHOICES = [
        (DAY, _('Daily')),
        (WEEK, _('Weekly')),
        (FORTNIGHT, _('Fortnight')),
        (MONTH, _('Monthly')),
        (QUATER, _('Quaterly')),
        (HALFYEAR, _('Half-yearly')),
        (YEAR, _('Yearly'))
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
    validity_delay = models.PositiveSmallIntegerField(
        _('Validity'), help_text='Medical Care Validity Delay!', default=0)
    standing = models.IntegerField(
        _('Standing'), choices=STANDING_CHOICES, default=None)
    is_gender_gontrol = models.BooleanField(
        _('Is Gender Control'), default=True)
    waiting_delay = models.PositiveSmallIntegerField(
        _('Waiting Delay'), default=0, help_text=_('Waiting delay in days.'))
    individual_ceiling = models.DecimalField(
        _('Individual Ceiling'), max_digits=9, decimal_places=0, default=0)
    family_ceiling = models.DecimalField(
        _('Family Ceiling'), max_digits=9, decimal_places=0, default=0)
    public_coverage = models.PositiveSmallIntegerField(_('Public Coverage'), validators=[
        MinValueValidator(0), MaxValueValidator(100)], default=0)
    private_coverage = models.PositiveSmallIntegerField(_('Private Coverage'), validators=[
        MinValueValidator(0), MaxValueValidator(100)], default=0)
    public_coverage = models.PositiveSmallIntegerField(_('Public Coverage'), validators=[
        MinValueValidator(0), MaxValueValidator(100)], default=0)
    public_claim = models.PositiveSmallIntegerField(_('Public Claim'), validators=[MinValueValidator(
        0), MaxValueValidator(100)], default=0)  # Remboursement Public Zone couverte
    private_claim = models.PositiveSmallIntegerField(_('Private Claim'), validators=[MinValueValidator(
        0), MaxValueValidator(100)], default=0)  # Remboursement Privé Zone couverte
    claim_delay = models.PositiveSmallIntegerField(
        _('Claim Delay'), help_text='Delay in days', default=0)
    max_claim = models.PositiveSmallIntegerField(
        _('Max Claim'), help_text='Maximum number of claims allowed', default=0)
    claim_ceilling = models.DecimalField(
        _('Claim Ceilling'), max_digits=9, decimal_places=0, help_text='Claim Ceilling Amount', default=0)
    individual_claim_ceiling = models.DecimalField(
        _('Individual Claim Ceiling'), max_digits=9, decimal_places=0, help_text='Individual Claim Ceiling Amount', default=0)
    family_claim_ceiling = models.DecimalField(
        _('Family Claim Ceiling'), max_digits=9, decimal_places=0, help_text='Family Claim Ceiling Amount', default=0)
    member_age_limit = models.PositiveSmallIntegerField(
        _('Member Age Limit'), help_text='Member Age Limit allowance', default=0)
    child_age_limit = models.PositiveSmallIntegerField(
        _('Child Age Limit'), help_text='Child Age Limit allowance', default=0)
    additional_child = models.PositiveSmallIntegerField(
        _('Additional Child'), help_text=_('Allowed Child Limited Number allowed!'), default=0)
    child_maxi = models.PositiveSmallIntegerField(
        _('Maximum Child'), help_text=_('Allowed Child Limited Number allowed!'), default=0)
    child_majority = models.PositiveSmallIntegerField(
        _('Child Majority Age'), help_text='Majority Age of child', default=0)
    spouse_age_limit = models.PositiveSmallIntegerField(
        _('Spouse Age Limit'), help_text='Spouse Age Limit allowance', default=0)
    additional_spouse = models.PositiveSmallIntegerField(
        _('Additional Spouse'), help_text=_('Allowed Spouse Limited Number allowed!'), default=0)
    spouse_maxi = models.PositiveSmallIntegerField(
        _('Maximum Spouse'), help_text=_('Allowed Spouse Limited Number allowed!'), default=0)
    insurance_premium = models.DecimalField(
        _('Insurance Premium'), max_digits=9, decimal_places=0, default=0)
    premium_cycle = models.IntegerField(
        _('Premium Cycle'), choices=PREMIUM_CYCLE_CHOICES, default=None)
    min_tolerated_amount = models.DecimalField(
        _('Min. Tolerated Amount'), max_digits=6, decimal_places=0, default=0)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

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

    subscription_plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.RESTRICT)
    category = models.ForeignKey(
        to='medical.MedicineCategory', on_delete=models.RESTRICT)
    gender = models.IntegerField(
        _('Gender'), choices=GENDER_CHOICES, default=None)
    relationship = models.IntegerField(
        _('Relationship'), choices=RELATIONSHIP_CHOICES, default=None)
    is_ticket_due = models.BooleanField(_('Is Ticket Due'), default=True)
    individual_maxi_service = models.PositiveSmallIntegerField(
        _('Maxi Svce/Person'), help_text=_('Maximum number services per Person'), default=0)
    family_maxi_service = models.PositiveSmallIntegerField(
        _('Maxi Svce/Family'), help_text=_('Maximum nummber services per family'), default=0)
    personal_ceiling = models.DecimalField(
        _('Ceiling/Person'), max_digits=9, decimal_places=0, default=0)
    family_ceiling = models.DecimalField(
        _('Ceiling/Ceiling'), max_digits=9, decimal_places=0, default=0)
    age_limit = models.PositiveSmallIntegerField(_('Age limit'), help_text=_(
        'Age limitation for allowing the service'), default=0)
    waiting_delay = models.PositiveSmallIntegerField(_('Waiting delay'), help_text=_(
        'Delay between two (2) services in days!'), default=0)
    service_timeOut = models.PositiveSmallIntegerField(_('Timeout'), help_text=_(
        'Waiting delay after registering in days!'), default=0)
    is_strict = models.BooleanField(_('Is strict'), default=False)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name_plural = _('Plan Categories')
        unique_together = ('category', 'subscription_plan')


class PlanCodification(models.Model):
    subscription_plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.RESTRICT)
    codification = models.ForeignKey(
        to='medical.Codification', on_delete=models.RESTRICT)
    public_rate = models.PositiveSmallIntegerField(_('Public Rate'), validators=[
        MinValueValidator(1), MaxValueValidator(100)], default=0)
    private_rate = models.PositiveSmallIntegerField(_('Private Rate'), validators=[
        MinValueValidator(1), MaxValueValidator(100)], default=0)
    claim_rate = models.PositiveSmallIntegerField(_('Claim Rate'), validators=[
        MinValueValidator(1), MaxValueValidator(100)], default=0)
    individual_ceiling = models.DecimalField(
        _('Indidual Ceiling'), max_digits=9, decimal_places=0, default=0)
    family_ceiling = models.DecimalField(
        _('Family Ceiling'), max_digits=9, decimal_places=0, default=0)
    ceiling_cmount = models.DecimalField(
        _('Ceiling Amount'), max_digits=9, decimal_places=0, default=0)
    waiting_delay = models.PositiveSmallIntegerField(
        _('Waiting Delay'), help_text=_('Waiting delay in days.'), default=0)
    is_strict = models.BooleanField(_('Is strict'), default=False)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.codification.code

    class Meta:
        unique_together = ('codification', 'subscription_plan')


class Subscriber(models.Model):
    # Subscriber models
    id_code = models.CharField(
        _("ID. Code"), max_length=50, unique=True, editable=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=32)
    matricule = models.CharField(max_length=12)
    locality = models.ForeignKey(
        Locality, on_delete=models.SET_NULL, null=True, blank=True)
    grouping = models.ForeignKey(
        Grouping, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    blood_group = models.IntegerField(
        choices=BLOOD_GRP_CHOICES, default=None, null=True, blank=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    # deceased_at = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    """ create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True) """
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def age(self):
        now = datetime.now()
        dob = self.date_of_birth
        dod = self.deceased_at
        if dod is not None:
            delta = relativedelta(dod, dob)
        else:
            delta = relativedelta(now, dob)
        return delta.years

    def save(self, *args, **kwargs):
        # 'department' is ForeignKey, has a 'code' field consisting of a 2-3 letter code.
        loc = str(self.locality.name[0:2])
        # gets the last 2 digits from the project start date year.
        # yy = str(self.create_at.year)[-2:]
        # makes a database query to find any matching Dept-Year combination in the 'project code' field
        filter_kw = '{}'.format(loc)
        # get the last record that has the same combination.
        lastrec = Subscriber.objects.filter(
            id_code__startswith=filter_kw).last()

        if not self.pk:  # this keeps the following instructions from executing if there already is a project code, i.e.: when updating record information.

            if lastrec == None:
                lastrec = '00'
                newrec = int(lastrec)+1
            elif lastrec.id_code == self.id_code:
                lastrec = str(lastrec.id_code)[-2:]
                newrec = int(lastrec)
            else:
                lastrec = str(lastrec.id_code)[-2:]
                newrec = int(lastrec)+1
            # the record should be in Charfield format, 2-digits, non-unique just in case there is a number above 99 (very unlikely)
            newnum = "{:08d}".format(int(newrec))
            self.id_code = '{}{}'.format(filter_kw, str(newnum))

        elif self.id_code == None:
            lastrec = '00'
            newrec = int(lastrec)+1

            newnum = "{:08d}".format(int(newrec))
            self.id_code = '{}{}'.format(filter_kw, str(newnum))
        else:
            pass

        super(Subscriber, self).save(*args, **kwargs)

    class Meta:
        ordering = ('first_name', 'last_name')


class Police(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.RESTRICT)
    subscription_plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.RESTRICT)
    begin_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.subscriber.lastName} {self.subscriber.firstName}"

    class Meta:
        unique_together = ('subscriber', 'subscription_plan')


class Assign(models.Model):
    SPOUSE = 0
    CHILD = 1

    RELATIONSHIP_CHOICES = [
        (SPOUSE, _('Spouse')),
        (CHILD, _('Child')),
    ]
    police = models.ForeignKey(
        Police, on_delete=models.RESTRICT, related_name='assigns')
    id_code = models.CharField(
        _("ID. Code"), max_length=50, unique=True, editable=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=32)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    date_of_birth = models.DateField(_('Date of birth'))
    relationship = models.IntegerField(
        _('Relationship'), choices=RELATIONSHIP_CHOICES, default=None)
    locality = models.ForeignKey(
        Locality, on_delete=models.SET_NULL, null=True, blank=True)
    grouping = models.ForeignKey(
        Grouping, on_delete=models.SET_NULL, null=True, blank=True)
    blood_group = models.IntegerField(
        choices=BLOOD_GRP_CHOICES, default=None, null=True, blank=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    # deceased_at = models.DateField(_('Deceased at'), null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_stopped = models.BooleanField(default=True)
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def age(self):
        now = datetime.now()
        dob = self.date_of_birth
        dod = self.deceased_at
        if dod is not None:
            delta = relativedelta(dod, dob)
        else:
            delta = relativedelta(now, dob)
        return delta.years


class Scholarship(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.RESTRICT)
    start_date = models.DateField(_('begin date'))
    end_date = models.DateField(_('end date'))
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.assign.fullName


class Suspension(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.RESTRICT)
    start_date = models.DateField(_('begin date'))
    end_date = models.DateField(_('end date'))
    reason = models.TextField(_('Suspension Reason'))
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.assign.fullName


class Decease(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.RESTRICT)
    assisgn = models.ForeignKey(
        Assign, on_delete=models.RESTRICT, blank=True, null=True)
    deceased_at = models.DateField(_('Deceased at'))
    note = models.TextField(blank=True, null=True)
