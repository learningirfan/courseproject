from django.db import models

# Create your models here.
class Exps(models.Model):
    date = models.DateField("Date", max_length=10, blank=False, null=False)
    amt = models.FloatField("Amount", max_length=9)
    cat = models.CharField("Category", max_length=15)
    ven = models.CharField("Vendor", max_length=20)
    cap = models.CharField("Caption", max_length=45)
    pmeth = models.CharField("Payment Method", max_length=20)

def __str__(self):
    return self.all
