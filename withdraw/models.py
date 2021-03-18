from django.db import models
from django.utils import timezone
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

class Withdraw(TimeStamp):
    withdraw_date = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField(default=0)
    by = models.ForeignKey(PersonDetail, on_delete=models.CASCADE)
    withdraw_method = models.CharField(max_length=150, choices=DEPOSIT_METHOD)
    institution = models.ForeignKey(InstitutionDetail, on_delete=models.CASCADE)
    is_business = models.BooleanField(default=False)
    is_personal = models.BooleanField(default=False)
    source = models.CharField(max_length=250, null=True, blank=True) 

    def __str__(self):
        return str(self.amount)
    
