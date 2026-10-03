from django.contrib import admin
from .models import CustomUser

# Register your models here.

class customerUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','role']
    list_filter = ['role']
    
admin.site.register(CustomUser,customerUserAdmin)
