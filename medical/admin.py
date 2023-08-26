from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from medical.models import MedicineCategory, Speciality, Codification, Pathology, \
    Nomenclature, Molecule, MedicationType, TherapeuticRoute, Medication, \
    CenterType, HealthCenter, Service, Practitioner, HealthCare, HealthCareItem, MedicationItem


@admin.register(Speciality)
class SpecialityAdmin(ImportExportModelAdmin):
    pass


@admin.register(MedicineCategory)  # Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Codification)
class CodificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Pathology)
class PathologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Nomenclature)
class NomenclatureAdmin(admin.ModelAdmin):
    pass


@admin.register(Molecule)
class MoleculeAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicationType)
class MedicationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(TherapeuticRoute)
class TherapeuticRouteAdmin(admin.ModelAdmin):
    pass


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    pass


@admin.register(CenterType)
class CenterTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Practitioner)
class PractitionerAdmin(admin.ModelAdmin):
    pass


class ServiceInline(admin.TabularInline):
    model = Service


@admin.register(HealthCenter)
class HealthCenterAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


class HealthCareItemInline(admin.TabularInline):
    model = HealthCareItem


class MedicationItemInline(admin.StackedInline):
    model = MedicationItem


@admin.register(HealthCare)
class HealthCareQdmin(admin.ModelAdmin):
    inlines = [HealthCareItemInline, MedicationItemInline]
