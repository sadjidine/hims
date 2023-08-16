from django.contrib import admin
from medical.models import Speciality, Category, Codification, Pathology, \
    Nomenclature, Molecule, MedicationType, TherapeuticRoute, Medication


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)  # Register your models here.
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
