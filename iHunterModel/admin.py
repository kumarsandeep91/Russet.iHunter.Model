from django.contrib import admin
from iHunterModel.models import *

iHunterModels = [
    Address, 
    Contact, 
    ContactType, 
    Organization,
    OrganizationType, 
    EducationalOrganization, 
    EducationalOrganizationType,
    Title,
    Person,
    Student,
    Gender,
    Country,
    State,
    City,
    ZipCode]

#admin.site.register(Address)
admin.site.register(iHunterModels)