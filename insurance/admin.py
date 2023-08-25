from django.contrib import admin

from insurance.models import SubscriptionPlan, PlanCategory, PlanCodification
# Register your models here.


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    pass
