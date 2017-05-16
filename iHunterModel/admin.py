from django.contrib import admin
from iHunterModel.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fields = ['title','first_name', 'middle_name', 'last_name', 'roll']

class TitleAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Student, StudentAdmin)
admin.site.register(Title, TitleAdmin)