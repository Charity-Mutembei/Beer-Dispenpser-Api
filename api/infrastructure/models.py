from django.db import models

# Create your models here.
class Dispense(models.Model):
    beerchoices = (
        ('Larger beer', 'Larger beer'),
        ('Pilsner beer', 'Pilsner beer'),
        ('Guness beer', 'Guness beer'),
    )
    productname = models.CharField(max_length=200, choices = beerchoices)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=2.00)
    dispensing_time = models.TimeField(blank=True, null=True)
    stop_dispensing_time = models.TimeField(blank=True, null=True)


    def __str__(self):
        return self.productname

    def save_dispense(self):
        self.save()