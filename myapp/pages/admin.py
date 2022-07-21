from django.contrib import admin
from .models import Page,Contactform,Profile

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ("title","update_date")
    ordering = ("title",)
    search_fields = ("title",)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("yourname","email")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username","gender","semester","email")

admin.site.register(Page,PageAdmin)
admin.site.register(Contactform,ContactAdmin)
admin.site.register(Profile,ProfileAdmin)