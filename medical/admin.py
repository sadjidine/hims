from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from medical.models import MedicineCategory, Speciality, Codification, Pathology, \
    Nomenclature, Molecule, MedicationType, TherapeuticRoute, Medication, \
    CenterType, HealthCenter, Service, Practitioner, HealthCare, HealthCareItem, MedicationItem, Staff


@admin.register(Speciality)
class SpecialityAdmin(ImportExportModelAdmin):
    pass


@admin.register(MedicineCategory)  # Register your models here.
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


@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin):
    pass


class StaffInline(admin.TabularInline):
    model = Staff
    extra = 0


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0


@admin.register(HealthCenter)
class HealthCenterAdmin(ImportExportModelAdmin):
    inlines = [ServiceInline, StaffInline]


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    pass


class HealthCareItemInline(admin.TabularInline):
    model = HealthCareItem
    extra = 0


class MedicationItemInline(admin.StackedInline):
    model = MedicationItem
    extra = 1


@admin.register(HealthCare)
class HealthCareAdmin(ImportExportModelAdmin):
    inlines = [HealthCareItemInline, MedicationItemInline]
