from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(ExpenseType, PaymentType, PaymentDetail)


@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass