from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

from core.models import Locality, Grouping
from insurance.models import SubscriptionPlan
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


class Subscriber(models.Model):
    # Subscriber models
    idCode = models.CharField(
        _("ID. Code"), max_length=50, unique=True, editable=False)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=32)
    matricule = models.CharField(max_length=12)
    locality = models.ForeignKey(
        Locality, on_delete=models.SET_NULL, null=True, blank=True)
    grouping = models.ForeignKey(
        Grouping, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    dateOfBirth = models.DateField(_('Date of birth'))
    bloodGrp = models.IntegerField(
        choices=BLOOD_GRP_CHOICES, default=None, null=True, blank=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    deceased_at = models.DateField(_('Deceased at'), null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    isActive = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.lastName} {self.firstName}"

    def fullName(self):
        return f"{self.lastName} {self.firstName}"

    def age(self):
        now = datetime.now()
        dob = self.dateOfBirth
        dod = self.deceased_at
        if dod is not None:
            delta = relativedelta(dod, dob)
        else:
            delta = relativedelta(now, dob)
        return delta.years

    def save(self, *args, **kwargs):
        # 'department' is ForeignKey, has a 'code' field consisting of a 2-3 letter code.
        dpt = str(self.department.code)
        # gets the last 2 digits from the project start date year.
        yy = str(self.create_at.year)[-2:]
        # makes a database query to find any matching Dept-Year combination in the 'project code' field
        filter_kw = '{}-{}-'.format(dpt, yy)
        # get the last record that has the same combination.
        lastrec = Subscriber.objects.filter(
            idCode__startswith=filter_kw).last()

        if not self.pk:  # this keeps the following instructions from executing if there already is a project code, i.e.: when updating record information.

            if lastrec == None:
                lastrec = '00'
                newrec = int(lastrec)+1
            elif lastrec.idCode == self.idCode:
                lastrec = str(lastrec.idCode)[-2:]
                newrec = int(lastrec)
            else:
                lastrec = str(lastrec.idCode)[-2:]
                newrec = int(lastrec)+1
            # the record should be in Charfield format, 2-digits, non-unique just in case there is a number above 99 (very unlikely)
            newnum = "{:02d}".format(int(newrec))
            self.idCode = '{}{}'.format(filter_kw, str(newnum))

        elif self.idCode == None:
            lastrec = '00'
            newrec = int(lastrec)+1

            newnum = "{:02d}".format(int(newrec))
            self.idCode = '{}{}'.format(filter_kw, str(newnum))
        else:
            pass

        super(Subscriber, self).save(*args, **kwargs)


class Police(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.RESTRICT)
    subscriptionPlan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.RESTRICT)
    beginDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.subscriber.lastName} {self.subscriber.firstName}"

    class Meta:
        unique_together = ('subscriber', 'subscriptionPlan')


class Assign(models.Model):
    SPOUSE = 0
    CHILD = 1

    RELATIONSHIP_CHOICES = [
        (SPOUSE, _('Spouse')),
        (CHILD, _('Child')),
    ]
    police = models.ForeignKey(Police, on_delete=models.RESTRICT)
    idCode = models.CharField(
        _("ID. Code"), max_length=50, unique=True, editable=False)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=32)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    dateOfBirth = models.DateField(_('Date of birth'))
    relationship = models.IntegerField(
        _('Relationship'), choices=RELATIONSHIP_CHOICES, default=None)
    locality = models.ForeignKey(
        Locality, on_delete=models.SET_NULL, null=True, blank=True)
    grouping = models.ForeignKey(
        Grouping, on_delete=models.SET_NULL, null=True, blank=True)
    bloodGrp = models.IntegerField(
        choices=BLOOD_GRP_CHOICES, default=None, null=True, blank=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    deceased_at = models.DateField(_('Deceased at'), null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    isActive = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.lastName} {self.firstName}"

    def fullName(self):
        return f"{self.lastName} {self.firstName}"

    def age(self):
        now = datetime.now()
        dob = self.dateOfBirth
        dod = self.deceased_at
        if dod is not None:
            delta = relativedelta(dod, dob)
        else:
            delta = relativedelta(now, dob)
        return delta.years


class Scholarship(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.RESTRICT)
    beginDate = models.DateField(_('begin date'))
    endDate = models.DateField(_('end date'))
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.assign.fullName


class Suspension(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.RESTRICT)
    beginDate = models.DateField(_('begin date'))
    endDate = models.DateField(_('end date'))
    reason = models.TextField(_('Suspension Reason'))
    create_at = models.DateField(
        _('Creation Date'), auto_now_add=True)
    modified_at = models.DateField(_('Modified Date'), auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.assign.fullName
