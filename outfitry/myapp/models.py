from django.db import models

# Create your models here.
#from django.db import models
#from django.contrib.auth.models import User
#from django.utils import timezone
#from decimal import Decimal

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_premium = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",
        blank=True,
    )

    def upgrade_to_premium(self):
        self.is_premium = True
        self.save()

class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('shoes', 'Shoes'),
        ('accessory', 'Accessory'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    
    image = models.ImageField(upload_to='clothing_items/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Outfit(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=100)
    tags = models.JSONField(default=list)  # Store tags as a list
    items = models.ManyToManyField(ClothingItem)

    image = models.ImageField(upload_to='outfit_images/', null=True, blank=True) # Add new

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggested_outfits = models.ManyToManyField(Outfit)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_for_user(self, user):
        # Implement recommendation logic here
        pass

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def renew_subscription(self):
        # Implement renewal logic here
        pass

