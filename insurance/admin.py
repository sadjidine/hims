from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from insurance.models import Membership, PlanCategory, PlanCodification, Patient, Subscriber, Subscription, Assign, Scholarship, Suspension, Decease, Claim, ClainItem


# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id_code', 'full_name', 'gender', 'age',
                    'parental_status', 'mobile_1', 'email')


@admin.register(Subscriber)
class SubscriberAdmin(ImportExportModelAdmin):
    list_display = ('id_code', 'full_name', 'matricule',
                    'gender', 'age', 'mobile_1', 'email')


@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    list_display = ('id_code', 'full_name', 'gender', 'age',
                    'relationship', 'mobile_1', 'email')


class AssignInline(admin.TabularInline):
    model = Assign
    extra = 0


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [AssignInline]


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


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    inlines = [PlanCategoryInline, PlanCodificationInline]


class ClaimItemInline(admin.TabularInline):
    model = ClainItem
    extra = 0


@admin.register(Claim)
class claimAdmin(admin.ModelAdmin):
    inlines = [ClaimItemInline]
