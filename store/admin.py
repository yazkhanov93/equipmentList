from django.contrib import admin
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["title",]


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "firstname", "middlename", "lastname", "department"]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(EquipmentList)
class EquipmentListAdmin(admin.ModelAdmin):
    list_display = ["equipmentId", "specificationId","fileName","dateCreate","dateModify"]