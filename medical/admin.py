from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from medical.models import Category, Speciality, Codification, Pathology, \
    Nomenclature, Molecule, MedicationType, TherapeuticRoute, Medication, \
    CenterType, HealthCenter, Agreement, CareService, Practitioner, HealthCare, CareItem, CareOnDemand, MedicationItem


@admin.register(Speciality)
class SpecialityAdmin(ImportExportModelAdmin):
    pass


@admin.register(Category)  # Register your models here.
class CategoryAdmin(ImportExportModelAdmin):
    pass


@admin.register(Codification)
class CodificationAdmin(ImportExportModelAdmin):
    pass


@admin.register(Pathology)
class PathologyAdmin(ImportExportModelAdmin):
    pass


@admin.register(Nomenclature)
class NomenclatureAdmin(ImportExportModelAdmin):
    pass


@admin.register(Molecule)
class MoleculeAdmin(ImportExportModelAdmin):
    pass


@admin.register(MedicationType)
class MedicationTypeAdmin(ImportExportModelAdmin):
    pass


@admin.register(TherapeuticRoute)
class TherapeuticRouteAdmin(ImportExportModelAdmin):
    pass


@admin.register(Medication)
class MedicationAdmin(ImportExportModelAdmin):
    pass


@admin.register(CenterType)
class CenterTypeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Practitioner)
class PractitionerAdmin(ImportExportModelAdmin):
    pass


# @admin.register(Staff)
# class StaffAdmin(ImportExportModelAdmin):
#     pass


# class StaffInline(admin.TabularInline):
#     model = Staff
#     extra = 0


class ServiceInline(admin.TabularInline):
    model = CareService
    extra = 0


@admin.register(HealthCenter)
class HealthCenterAdmin(ImportExportModelAdmin):
    pass


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


@admin.register(CareService)
class ServiceAdmin(ImportExportModelAdmin):
    pass


class HealthCareItemInline(admin.TabularInline):
    model = CareItem
    extra = 0


class CareOnDemandItemInline(admin.TabularInline):
    model = CareOnDemand
    extra = 0


class MedicationItemInline(admin.StackedInline):
    model = MedicationItem
    extra = 1


@admin.register(HealthCare)
class HealthCareAdmin(ImportExportModelAdmin):
    inlines = [HealthCareItemInline,
               CareOnDemandItemInline, MedicationItemInline]
