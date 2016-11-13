from django.contrib import admin
from .models import person

class personAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Person Details", {"fields":["name", "id_number", "address", "age", "date_added"]}),
    ]
    ordering = ['name']
    actions = ['delete']
    readonly_fields = ("date_added",)
    list_display = ("name","date_added")
    list_display_links = ("name", "date_added")
    search_fields = ("name","address","age")
# Register your models here.
admin.site.register(person,personAdmin)
