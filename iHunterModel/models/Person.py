from iHunterModel.models import DomainObject
from django.db import models

# title or designation
class Title(DomainObject):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

# gender or sex
class Gender(DomainObject):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

# abstract base class for all person.
class Person(DomainObject):
    # title for the person i.e Mr. Mrs. Doctor etc. Relationship
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True)
    
    first_name = models.CharField(max_length=255, blank=False)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    # relationship
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name