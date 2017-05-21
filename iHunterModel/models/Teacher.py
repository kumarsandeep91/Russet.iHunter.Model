from iHunterModel.models import Person, EducationalOrganization
from django.db import models

# student class
class Teacher(Person):
    
    # relationships
    # a student can belong to many educational organizations.
    educational_organizations = models.ManyToManyField('EducationalOrganization')

    def __str__(self):
        return self.first_name