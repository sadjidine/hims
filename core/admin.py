from django.contrib import admin
from core.models import Company, Exercice, Grouping, District, Region, Locality


# Register your models here.



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Grouping)
class GroupingAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    pass

