from iHunterModel.models import DomainObject, Title
from django.db import models

# abstract base class for all person.
class Person(DomainObject):
    # title for the person i.e Mr. Mrs. Doctor etc.
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=False)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True