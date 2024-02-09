from django.contrib import admin

# Register your models here.

from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['sname','sprinc','sloc']

class cust2(admin.ModelAdmin):
    list_display = ['stdname','stdage','sname']

admin.site.register(School,cust)

admin.site.register(Student,cust2)