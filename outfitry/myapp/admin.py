from django.contrib import admin
# Register your models here.
from .models import User, ClothingItem, Outfit, Recommendation, Subscription

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_premium', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_premium', 'is_staff', 'is_active')

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color', 'material')
    search_fields = ('name', 'category', 'color')

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('name', 'style')
    search_fields = ('name', 'style')
    filter_horizontal = ('items',)

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ('created_at',)
    filter_horizontal = ('suggested_outfits',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')

