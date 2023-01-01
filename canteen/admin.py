from django.contrib import admin
from .models import FoodItem

# Register your models here.
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image')