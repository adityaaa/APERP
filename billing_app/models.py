from django.db import models
# from billing_app.models import InventoryItem

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    full_address = models.TextField(default='')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=20, default='')
    drug_license_number = models.CharField(max_length=50, default='')
    gstin_number = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name
    
class Salt(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name    
    
class InventoryItem(models.Model):
    CATEGORY_CHOICES = [
        ('OTHER', 'Other Product'),
        ('POWDER', 'Powder'),
        ('SERVICE', 'Service'),
        ('SYRUP', 'Syrup / Suspensions'),
        ('TABLET', 'Tablet'),
    ]

    name = models.CharField(max_length=100)
    packing = models.CharField(max_length=50)
    company = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    salt = models.ForeignKey(Salt, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    hsn = models.CharField(max_length=10, default='')

    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default="")
    conversion_strip = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    conversion_case = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    sgst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name