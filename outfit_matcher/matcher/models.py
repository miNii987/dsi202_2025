# from django.db import models

# class ClothingItem(models.Model):
#     ITEM_TYPES = (
#         ('shirt', 'Shirt'),
#         ('pants', 'Pants'),
#         ('jacket', 'Jacket'),
#     )
    
#     STYLES = (
#         ('casual', 'Casual'),
#         ('formal', 'Formal'),
#     )
    
#     item_type = models.CharField(max_length=50, choices=ITEM_TYPES)
#     color = models.CharField(max_length=50)
#     style = models.CharField(max_length=50, choices=STYLES)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.item_type} - {self.color} ({self.style})"

from django.db import models

class ClothingItem(models.Model):
    ITEM_TYPES = (
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('dress', 'Dress'),
    )
    
    STYLES = (
        ('formal', 'Formal'),
        ('bussiness', 'Bussiness'),
        ('business casual', 'Business Casual'),
        ('smart casual', 'Smart Casual'),
        ('casual', 'Casual'),

    )
    
    item_type = models.CharField(max_length=50, choices=ITEM_TYPES)
    color = models.CharField(max_length=50)
    style = models.CharField(max_length=50, choices=STYLES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.item_type} - {self.color} ({self.style})"
    
    
