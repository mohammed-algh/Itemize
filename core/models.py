from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    warranty_expiry = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def short_description(self):
        return self.description[:30] + '...' if len(self.description) > 30 else self.description
    
    def is_warranty_valid(self):
        if self.warranty_expiry:
            from django.utils import timezone
            return timezone.now().date() <= self.warranty_expiry
        return False