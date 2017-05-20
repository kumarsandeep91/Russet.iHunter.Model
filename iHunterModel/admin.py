from django.contrib import admin
from iHunterModel.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fields = ['title','first_name', 'middle_name', 'last_name', 'gender', 'roll']

class TitleAdmin(admin.ModelAdmin):
    fields = ['name']

class GenderAdmin(admin.ModelAdmin):
    fields = ['name']

class OrganizationTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class EducationalOrganizationTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class EducationalOrganizationAdmin(admin.ModelAdmin):
    fields = ['logo', 'name', 'legal_name', 'type', 'category']

admin.site.register(Student, StudentAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(OrganizationType, OrganizationTypeAdmin)
admin.site.register(EducationalOrganizationType, EducationalOrganizationTypeAdmin)
admin.site.register(EducationalOrganization, EducationalOrganizationAdmin)