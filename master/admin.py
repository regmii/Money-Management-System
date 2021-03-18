from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(InstitutionType)
class InstitutionTypeAdmin(admin.ModelAdmin):
    pass 

@admin.register(InstitutionDetail)
class InstitutionDetail(admin.ModelAdmin):
    pass