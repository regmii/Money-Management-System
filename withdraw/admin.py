from django.contrib import admin
from .models import *
# Register your models here.

# @admin.register(DepositMethod)
# class DepositMethodAdmin(admin.ModelAdmin):
#     pass


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    pass