from django.contrib import admin
from .models import Page,Contactform

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ("title","update_date")
    ordering = ("title",)
    search_fields = ("title",)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("yourname","email")

admin.site.register(Page,PageAdmin)
admin.site.register(Contactform,ContactAdmin)