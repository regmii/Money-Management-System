from django.db import models
from django.utils import timezone
from master.models import InstitutionDetail
from deposit.constants import DEPOSIT_METHOD, PURPOSE
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

class Withdraw(TimeStamp):
    withdraw_date = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField(default=0)
    by = models.ForeignKey(PersonDetail, on_delete=models.CASCADE)
    withdraw_method = models.CharField(max_length=150, choices=DEPOSIT_METHOD)
    institution = models.ForeignKey(InstitutionDetail, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200, choices=PURPOSE, default='1')
    source = models.CharField(max_length=250, null=True, blank=True) 

    def __str__(self):
        return str(self.amount)
    
