from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from membership.models import Subscriber, Police, Assign, Scholarship, Suspension
# Register your models here.


@admin.register(Subscriber)
class SubscriberAdmin(ImportExportModelAdmin):
    pass


@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    pass


@admin.register(Scholarship)
class ScolarshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Suspension)
class SuspensionAdmin(admin.ModelAdmin):
    pass
