from iHunterModel.models import Person, EducationalOrganization, Standard
from django.db import models

# student class
class Student(Person):
    
    # relationships
    # a student belongs to a standard or class.
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, blank=False, null=False) # required
    # a student can belong to many educational organizations.
    educational_organizations = models.ManyToManyField('EducationalOrganization')

    def __str__(self):
        return self.first_name