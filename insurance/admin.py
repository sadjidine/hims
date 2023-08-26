from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from insurance.models import SubscriptionPlan, PlanCategory, PlanCodification, Subscriber, Police, Assign, Scholarship, Suspension, Decease


# Register your models here.
@admin.register(Subscriber)
class SubscriberAdmin(ImportExportModelAdmin):
    list_display = ('id_code', 'full_name', 'matricule',
                    'date_of_birth', 'age', 'mobile', 'email')


@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    pass


@admin.register(Scholarship)
class ScolarshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Suspension)
class SuspensionAdmin(admin.ModelAdmin):
    pass


@admin.register(Decease)
class deceaseAdmin(admin.ModelAdmin):
    pass


class PlanCategoryInline(admin.TabularInline):
    model = PlanCategory


class PlanCodificationInline(admin.TabularInline):
    model = PlanCodification
    extra = 0


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    inlines = [PlanCategoryInline, PlanCodificationInline]
