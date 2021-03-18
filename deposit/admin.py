from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(PersonDetail)
class PersonDetailAdmin(admin.ModelAdmin):
    pass


# @admin.register(DepositMethod)
# class DepositMethodAdmin(admin.ModelAdmin):
#     pass


@admin.register(Deposits)
class DepositsAdmin(admin.ModelAdmin):
    pass