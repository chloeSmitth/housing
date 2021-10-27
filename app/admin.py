from django.contrib import admin
from .models import Housing, Style, Amenitie


class HousingAdmin(admin.ModelAdmin):
    list_display = ["name", "housing_type", "address"]
    ordering = ["housing_type", "name"]

class StyleAdmin(admin.ModelAdmin):
    list_display = ["name", "beds", "baths", "people", "rent"]
    ordering = ['name', "beds", "baths", "people", "rent"]


admin.site.register(Amenitie)
admin.site.register(Housing, HousingAdmin)
admin.site.register(Style, StyleAdmin)

# Register your models here.
