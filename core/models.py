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


class Company(models.Model):
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=32, unique=True)
    address = models.CharField(max_length=64, null=True)
    # logo = models.ImageField(upload_to='images')
    note = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"({self.acronym}){self.acronym}"

    class Meta:
        verbose_name_plural = _("Companies")


class Exercice(models.Model):
    title = models.CharField(max_length=64)
    start_at = models.DateField()
    end_at = models.DateField()
    medical_care_validity = models.SmallIntegerField()
    medication_margin = models.DecimalField(max_digits=6, decimal_places=0)
    closed = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.company.name}"

    def save(self, *args, **kwargs):
        if self.start_at > self.end_at:
            raise ValidationError(
                _("The start date must be less than or equal to the end date!"),
            )
        super(Exercice, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('title', 'company')


class Grouping(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.company.name}"

    class Meta:
        unique_together = ('name', 'company')


class District(models.Model):
    name = models.CharField(max_length=64)
    country = CountryField()
    note = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.country.name}"

    class Meta:
        unique_together = ('name', 'country')


class Region(models.Model):
    name = models.CharField(max_length=64)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.district.name}"

    class Meta:
        unique_together = ('name', 'district')


class Locality(models.Model):
    name = models.CharField(max_length=64)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.region.name}"

    class Meta:
        unique_together = ('name', 'region')
        verbose_name_plural = _("Localities")
