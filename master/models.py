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



class InstitutionType(TimeStamp):
    institution_type = models.CharField(max_length=200)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.institution_type


class InstitutionDetail(TimeStamp):
    institution_type = models.ForeignKey(InstitutionType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    balance = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name
