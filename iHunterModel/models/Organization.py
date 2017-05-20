from iHunterModel.models import DomainObject
from django.db import models

# class for specifying different types of orgs. like public, gov., private etc.
class OrganizationType(DomainObject):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name

# Abstract class for all organization entities.
class Organization(DomainObject):
    # This field is not nullable or blank
    name = models.CharField(max_length=255, null=False, blank=False)
    legal_name = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='uploads/images/logos/', default='uploads/images/logos/default/organization.png')

    # Relationship. nullable is true.
    type = models.ForeignKey(OrganizationType, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True