from iHunterModel.models import DomainObject, Organization
from django.db import models

# class for specifying different types of EduOrgs. like school, colleges, universities etc.
class EducationalOrganizationType(DomainObject):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name

class EducationalOrganization(Organization):
    

    # Relationship. nullable is true.
    category = models.ForeignKey(EducationalOrganizationType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name