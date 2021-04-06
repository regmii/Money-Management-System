from django.db import models
from django.utils import timezone
from master.models import InstitutionDetail
from .constants import DEPOSIT_METHOD, PURPOSE
# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

class PersonDetail(TimeStamp):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Deposits(TimeStamp):
    deposit_date = models.DateTimeField(auto_now=True)
    account_no = models.CharField(max_length=300)
    amount = models.PositiveIntegerField()
    by = models.ForeignKey(PersonDetail, on_delete=models.CASCADE)
    deposit_method = models.CharField(max_length=150, choices=DEPOSIT_METHOD)
    institution = models.ForeignKey(InstitutionDetail, on_delete=models.CASCADE)
    branch = models.CharField(max_length=200, default='')
    purpose = models.CharField(max_length=200, choices=PURPOSE)
    business_name = models.CharField(max_length=200, null=True, blank=True)
    source_of_deposit = models.CharField(max_length=300, blank=True, null=True)
    source = models.CharField(max_length=250, null=True, blank=True) 
    cheque_no = models.CharField(max_length=200, blank=True, null=True)
    cheque_image = models.ImageField(upload_to='images/cheque_images/', null=True, blank=True)
    deposit_slip_image = models.ImageField(upload_to='images/deposit_slip', null=True, blank=True)

    def __str__(self):
        return str(self.amount)

        
    
