from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug":("title",)}


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]


@admin.register(EquipmentList)
class EquipmentListAdmin(admin.ModelAdmin):
    list_display = ["equipmentId","specificationId", "fileName", "dateCreate", "dateModify"]


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "firstname", "middlename", "lastname","department"]
    list_editable = ["firstname", "middlename", "lastname", "department"]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["title"]