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

from medical.models import Speciality

# Create your models here.


class Degree(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            verbose_name=_('Degree name'))
    isActive = models.BooleanField(default=True)
    note = models.TextField()

    def __str__(self):
        return self.name


class Practionner(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    CorpReference = models.CharField(max_length=32)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=128)
    degree = models.ForeignKey(
        Degree, on_delete=models.PROTECT, null=True, blank=True)
    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT, null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=MALE)
    dateOfBirth = models.DateField(null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.lastName} - {self.firstName}"

    class Meta:
        unique_together = ('firstName', 'lastName', 'dateOfBirth')


class Standing(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rank = models.IntegerField(default=1,)
    note = models.TextField()
    isActive = models.BooleanField(default=True)
