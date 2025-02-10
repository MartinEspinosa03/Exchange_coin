from django.db import models

# Create your models here.

class ExchangeRate(models.Model):
    date = models.DateField(unique=True)
    rate = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.date}: {self.rate}"
    
class ExchangeRateDOF(models.Model):
    date = models.DateField(unique=True)
    currency_exchange = models.DecimalField(max_digits=10, decimal_places=4)
    
    def __str__(self):
        return f"{self.date} - {self.currency_exchange}"