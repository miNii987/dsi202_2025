# from django.contrib import admin
# from .models import ClothingItem

# @admin.register(ClothingItem)
# class ClothingItemAdmin(admin.ModelAdmin):
#     list_display = ('item_type', 'color', 'style', 'created_at')
#     list_filter = ('item_type', 'style')
#     search_fields = ('item_type', 'color')


from django.contrib import admin
from .models import ClothingItem

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'color', 'style')
    list_filter = ('item_type', 'style')
    search_fields = ('item_type', 'color')
    fields = ('item_type', 'color', 'style', 'image')  # Include image in admin form


