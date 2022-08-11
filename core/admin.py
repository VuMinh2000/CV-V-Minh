from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'create_at']
    search_fields = ['name', 'email', 'subject']
    list_per_page = 6


admin.site.register(Contact, ContactAdmin)
