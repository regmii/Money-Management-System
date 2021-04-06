from django.db import models
from django.utils import timezone
from deposit.models import PersonDetail
# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

class ContactType(TimeStamp):
    contact_type = models.CharField(max_length=300)

    # def __str__(self):
    #     return self.contact_type


class Contact(TimeStamp):
    contact_number = models.CharField(max_length=10)
    contact_type = models.ManyToManyField(ContactType)

    def __str__(self):
        return self.contact_number

class PaymentDetail(TimeStamp):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    choices = (
        ('Cash', 'Cash'), 
        ('Cheque', 'Cheque'), 
        ('Credit', 'Credit'), 
        ('E-Payment', 'E-Payment'), 
    )

    payment_type =models.CharField(max_length=200, choices=choices, default="Cash")
    type = (
        ('Cost of goods sold', 'Cost of goods sold'),
        ('Selling and distribution expenses', 'Selling and distribution expenses'),
        ('Operating, general and administrative expenses', 'Operating, general and administrative expenses'),
        ('Salaries, wages, and benefits', 'Salaries, wages, and benefits'),
        ('Rent expense', 'Rent expense'),
        ('Cost of utilities', 'Cost of utilities'),
        ('Provisions and impairments', 'Provisions and impairments'),
        ('Depreciation expense', 'Depreciation expense'),
        ('Amortization expense', 'Amortization expense'),
        ('Printing and stationery expense', 'Printing and stationery expense'),
        ('Staff traveling expense', 'Staff traveling expense'),
        ('Repair and maintenance expense', 'Repair and maintenance expense'),
        ('Insurance cost', 'Insurance cost'),
        ('Legal and professional charges', 'Legal and professional charges'),
        ('Communication expense', 'Communication expense'),
        ('Miscellaneous expenses', 'Miscellaneous expenses'),
        ('Finance cost', 'Finance cost'),
        ('Taxation', 'Taxation'),
    )
    expense_type = models.CharField(max_length=300, choices=type, default="Cost of goods sold")
    expense_sub_category = models.CharField(max_length=300)
    invoice_number = models.CharField(max_length=300)
    invoice_image = models.ImageField(upload_to='images/invoice_images/', null=True, blank=True)
    amount = models.PositiveIntegerField()
    cheque_no = models.CharField(max_length=200, null=True, blank=True)
    cheque_image = models.ImageField(upload_to='images/cheque_images/', null=True, blank=True)
    payment_made_to = models.ForeignKey(PersonDetail, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return self.name  

