from django.contrib import admin
from ticaretapp.models import Ticaret

# Register your models here.

class TicaretAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username Group',{"fields":["username"]})
    ]
    
admin.site.register(Ticaret,TicaretAdmin)